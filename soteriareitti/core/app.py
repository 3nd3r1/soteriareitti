# soteriareitti/soteriareitti.py
import logging

from geopy.distance import geodesic

from core.graph import Graph


class SoteriaReitti:
    def __init__(self):

        self._graph = Graph()

        self._graph.create_graph()
        logging.debug("SoteriaReitti initialized")

    def get_closest_node(self, location: tuple[float, float]):
        min_distance = 100
        closest_node = None

        for node in self._graph.nodes:
            logging.debug(node)
            distance = geodesic(location, node.location)
            if distance.m < min_distance:
                min_distance = distance.m
                closest_node = node

        return closest_node
