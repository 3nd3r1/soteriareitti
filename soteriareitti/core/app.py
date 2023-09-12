# soteriareitti/soteriareitti.py
import logging
import overpy

from core.graph import Graph
from utils.utils_geo import Location


class SoteriaReitti:
    def __init__(self):

        self._graph = Graph()
        self._graph.create_graph()

        logging.debug("SoteriaReitti initialized")

    def get_closest_node(self, location: Location) -> overpy.Node | None:
        closest_node = self._graph.get_closest_node(location)
        return closest_node
