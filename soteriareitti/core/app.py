""" soteriareitti/core/app.py """
import logging
from core.map import Map
from utils.utils_geo import Location
from utils.utils_graph import Node


class SoteriaReitti:
    def __init__(self, place: str):

        self._map = Map(place)

        logging.debug("SoteriaReitti initialized")

    def get_path(self, source: Location, target: Location) -> list[Node] | None:
        logging.debug("Getting path from %s to %s", source, target)
        source = self._map.get_closest_node(source)
        target = self._map.get_closest_node(target)

        if not source or not target:
            return None

        return self._map.get_shortest_path(source, target)
