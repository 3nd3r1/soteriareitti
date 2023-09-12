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
        pass
