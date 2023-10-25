""" soteriareitti/core/map.py """
import logging
import pickle
import overpy

from soteriareitti.core._overpass import OverpassAPI

from soteriareitti.algorithms.dijkstra import Dijkstra
from soteriareitti.algorithms.ida_star import IdaStar

from soteriareitti.classes.graph import Graph, Node, Edge, Path
from soteriareitti.classes.geo import Location, Distance, Speed

from soteriareitti.utils.graph import GraphUtils
from soteriareitti.utils.geo import GeoUtils
from soteriareitti.utils.file_reader import get_data
from soteriareitti.utils.settings import Settings


class DeprecatedCache(Exception):
    """ Raised when deprecated cache is loaded """


class Map:
    """ Map class that contains all the data and methods for the map """

    def __init__(self):
        self._overpass_api = OverpassAPI()
        self._graph = Graph()

        self._place = None
        self._average_speed = Speed(40)
        self._bounding_box = [float("inf"), float("inf"), float("-inf"), float("-inf")]

    def load_place(self, place: str):
        self._place = place
        if Settings.caching:
            try:
                self.__load_cached_graph()
            except (OSError, IOError, DeprecatedCache):
                self.__create_graph()
                self.__save_graph()
        else:
            self.__create_graph()

    def __save_graph(self):
        """ Save graph to pickle file """
        with open(get_data(f"{self._place}-graph.pickle"), "wb") as file:
            pickle.dump((Settings.cache_version, self._place,
                        self._average_speed, self._bounding_box, self._graph), file)
        logging.debug("Saved graph (%s) to pickle file", self._graph)

    def __load_cached_graph(self):
        """ Load graph from pickle file """
        with open(get_data(f"{self._place}-graph.pickle"), "rb") as file:
            cache_data = pickle.load(file)
            if cache_data[0] != Settings.cache_version:
                logging.debug("Trying to load deprecated cache version: %s, current version: %s",
                              cache_data[0], Settings.cache_version)
                raise DeprecatedCache
        self._place = cache_data[1]
        self._average_speed = cache_data[2]
        self._bounding_box = cache_data[3]
        self._graph = cache_data[4]
        logging.debug("Loaded graph (%s) from pickle file", self._graph)

    def __create_graph(self):
        """ 
        Create graph from data

        - Edges from and to an interesection have a speed limit of 30km/h
          this is because turning requires slowing down
        - Other edges have the speed limit of the road + 30kmh/h
        """
        logging.debug("Starting graph creation")
        # Create empty graph
        self._graph = Graph()

        # Get data from overpass api
        data = self._overpass_api.get_place_data(self._place)

        # Add all revieved nodes to graph
        logging.debug("Adding nodes to graph...")
        for node in data.nodes:
            if not node.lat or not node.lon:
                continue
            self._bounding_box[0] = min(self._bounding_box[0], float(node.lat))
            self._bounding_box[1] = min(self._bounding_box[1], float(node.lon))
            self._bounding_box[2] = max(self._bounding_box[2], float(node.lat))
            self._bounding_box[3] = max(self._bounding_box[3], float(node.lon))
            self._graph.add_node(str(node.id), location=Location(float(node.lat), float(node.lon)))
        logging.debug("Nodes added")

        logging.debug("Adding ways to graph...")

        # For each way (road) add edges between nodes
        for way in data.ways:
            one_way = way.tags.get("oneway", "no") == "yes"

            maxspeed = Speed(float(way.tags.get("maxspeed", "30"))+30)

            nodes = [str(node.id) for node in way.nodes]
            self._graph.nodes.get(nodes[0]).update(maxspeed=Speed(30))
            self._graph.nodes.get(nodes[-1]).update(maxspeed=Speed(30))

            for node_id in nodes[1:-1]:
                self._graph.nodes.get(node_id).update(maxspeed=maxspeed)

            for edge in list(zip(nodes[:-1], nodes[1:])):
                node_source = self._graph.nodes.get(edge[0])
                node_target = self._graph.nodes.get(edge[1])
                if not node_source or not node_target:
                    continue

                time = GeoUtils.calculate_time(
                    node_source.location, node_target.location,
                    min(node_source.maxspeed, node_target.maxspeed,
                        key=lambda s: s.kilometers_hour))
                self._graph.add_edge(node_source, node_target, cost=time.minutes)

                # If road is not one way, add edges from both directions
                if not one_way:
                    self._graph.add_edge(node_target, node_source, cost=time.minutes)

        logging.debug("Ways added")
        # Get largest component from graph so all nodes are connected

        logging.debug("Getting largest component from graph...")
        self._graph = GraphUtils.get_largest_component(self._graph)
        logging.debug("Largest component got")

        logging.debug("Created graph: %s", self._graph)

    def get_closest_node(self, location: Location) -> Node | None:
        """ Get closest node from a location that is atleast 50 meters close"""
        logging.debug("Getting closest node from %s", location)

        min_distance = Distance(50)
        closest_node = None

        data = self._overpass_api.get_around_data(location, min_distance)
        data_nodes: list[overpy.Node] = data.nodes

        for node in data_nodes:
            if str(node.id) not in self._graph.nodes:
                continue

            graph_node = self._graph.nodes[str(node.id)]
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
        def heuristic(node: Node, target_node: Node) -> float:
            """ Minutes to travel from node to target node """
            return GeoUtils.calculate_time(node.location,
                                           target_node.location, self._average_speed).minutes

        logging.debug("Getting shortest path from %s to %s", source, target)

        source_node = self.get_closest_node(source)
        target_node = self.get_closest_node(target)

        if not source_node or not target_node:
            logging.debug("No closest node found at source or target location.")
            return None

        path = IdaStar.get_shortest_path(
            self._graph, heuristic, source_node, target_node, delta=0.1)

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

        dijkstra_to_data = Dijkstra.get_data(reverse_graph, closest_node)
        dijkstra_from_data = Dijkstra.get_data(self._graph, closest_node)

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

    @property
    def bounding_box(self) -> list[float, float, float, float]:
        return self._bounding_box

    @property
    def place(self) -> str | None:
        return self._place
