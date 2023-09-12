# soteriareitti/soteriareitti.py
import logging

from core.graph import Graph
from utils.utils_geo import Location


class SoteriaReitti:
    def __init__(self, user_interface):

        self._ui = user_interface
        self._graph = Graph(user_interface)

        self._graph.create_graph()

        logging.debug("SoteriaReitti initialized")

    def get_closest_node(self, location: Location):
        """ Get closest node from a location that is atleast 100 meters close"""
        self._graph.get_closest_node(location)
