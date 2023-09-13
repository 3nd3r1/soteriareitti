""" soteriareitti/core/map.py """
import logging

from core._overpass import OverpassAPI
from utils.utils_graph import GraphUtils, Graph, Node
from utils.utils_geo import GeoUtils, Location, Distance


class Map:
    def __init__(self):
        self._overpass_api = OverpassAPI()

        self._graph = Graph()
        self.__create_graph()

    def __create_graph(self):
        logging.debug("Starting graph creation")

        data = self._overpass_api.get_place_data("Töölö")

        self._graph.add_nodes_from(data.nodes)

        for way in data.ways:
            self._graph.add_edges_from(list(way.nodes))

        # self._graph = GraphUtils.get_largest_component(self._graph)

        logging.debug("Graph creation done")

    def get_shortest_path(self, source: Node, target: Node) -> list[Node] | None:
        """ Get shortest path from source to target """
        if source.id not in self._graph.nodes or target.id not in self._graph.nodes:
            return None

    def get_closest_node(self, location: Location) -> Node | None:
        """ Get closest node from a location that is atleast 50 meters close"""
        logging.debug("Getting closest node from %s", location)

        min_distance = Distance(50)
        closest_node = None

        data = self._overpass_api.get_around_data(location, min_distance)
        data_nodes = [Node.from_overpy_node(node) for node in data.nodes]

        for node in data_nodes:
            if node.id not in self._graph.nodes:
                continue

            distance_to_center = GeoUtils.calculate_distance(
                location, node.location)

            if distance_to_center.meters < min_distance.meters:
                closest_node = node
                min_distance = distance_to_center

        if not closest_node:
            logging.debug("No nodes found")
        else:
            logging.debug("Closest node found: %s", closest_node)

        return closest_node
