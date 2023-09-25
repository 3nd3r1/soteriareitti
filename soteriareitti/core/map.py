""" soteriareitti/core/map.py """
import logging
import overpy

from soteriareitti.core._overpass import OverpassAPI
from soteriareitti.utils.graph import GraphUtils, Graph, Node, Edge, Path
from soteriareitti.utils.geo import GeoUtils, Location, Distance


class Map:
    """ Map class that contains all the data and methods for the map """

    def __init__(self, place: str):
        self._overpass_api = OverpassAPI()
        self._graph = Graph()
        self._place = place

        self.__create_graph()

    def __create_graph(self):
        """ Create graph from data """
        logging.debug("Starting graph creation")

        # Get data from overpass api
        data = self._overpass_api.get_place_data(self._place)

        # Add all revieved nodes to graph
        self._graph.add_nodes_from(data.nodes)

        # For each way (road) add edges between nodes
        for way in data.ways:
            one_way = way.tags.get("oneway", "no") == "yes"

            self._graph.add_edges_from(list(zip(way.nodes[:-1], way.nodes[1:])))

            # If road is not one way, add edges from both directions
            if not one_way:
                self._graph.add_edges_from(list(zip(way.nodes[1:], way.nodes[:-1])))

        # Get largest component from graph so all nodes are connected
        self._graph = GraphUtils.get_largest_component(self._graph)

        logging.debug("Created graph: %s", self._graph)

    def get_closest_node(self, location: Location) -> Node | None:
        """ Get closest node from a location that is atleast 50 meters close"""
        logging.debug("Getting closest node from %s", location)

        min_distance = Distance(50)
        closest_node = None

        data = self._overpass_api.get_around_data(location, min_distance)
        data_nodes: list[overpy.Node] = data.nodes

        for node in data_nodes:
            if node.id not in self._graph.nodes:
                continue

            graph_node = self._graph.nodes[node.id]
            distance_to_center = GeoUtils.calculate_distance(
                location, graph_node.location)

            if distance_to_center.meters < min_distance.meters:
                closest_node = graph_node
                min_distance = distance_to_center

        if not closest_node:
            logging.debug("No nodes found")
        else:
            logging.debug("Closest node found: %s", closest_node)

        return closest_node

    def get_shortest_path(self, source: Location, target: Location) -> Path | None:
        """ Get shortest path from source to target """

        logging.debug("Getting shortest path from %s to %s", source, target)

        source_node = self.get_closest_node(source)
        target_node = self.get_closest_node(target)

        if not source_node or not target_node:
            logging.debug("No closest node found at source or target location.")
            return None

        path = GraphUtils.ida_star_shortest_path(self._graph, source_node, target_node)

        if path:
            logging.debug("Shortest path found: %s", path)
        else:
            logging.debug("No path found")

        return path

    def get_dijkstra_data(self, location: Location) -> dict[dict, dict]:
        """ 
        Generate dijkstra data that contains shortest path
        from all nodes to location and from location to all nodes 
        """

        logging.debug("Generating dijkstra data from/to %s", location)
        reverse_graph = GraphUtils.reverse_graph(self._graph)
        closest_node = self.get_closest_node(location)

        if not closest_node:
            raise ValueError(f"{location} does not have any nodes close enough")

        dijkstra_to_data = GraphUtils.dijkstras_algorithm(reverse_graph, closest_node)
        dijkstra_from_data = GraphUtils.dijkstras_algorithm(self._graph, closest_node)

        logging.debug("Dijkstra data generated")
        return {"to": dijkstra_to_data, "from": dijkstra_from_data}

    def reconstruct_path(self, location_source: Location, location_target: Location,
                         dijkstra_data: dict[str, Edge]) -> Path | None:
        """ Reconstruct path from dijkstra data """

        logging.debug("Reconstructing path from %s to %s", location_source, location_target)
        node_source = self.get_closest_node(location_source)
        node_target = self.get_closest_node(location_target)

        if not node_source or not node_target:
            logging.debug("Source or target node not found")
            return None

        path = GraphUtils.reconstruct_path(dijkstra_data, node_source, node_target)

        if path:
            logging.debug("Path reconstructed: %s", path)

        return path
