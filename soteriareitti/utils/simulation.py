""" soteriareitti/utils/simulation.py """
import time
import random

from soteriareitti.core.map import Map
from soteriareitti.core.responder import Responder

from soteriareitti.classes.geo import Time, Location
from soteriareitti.classes.graph import Path


class ResponderSimulator:
    """
      This class is used to simulate a single responder moving around the map

        args:
            - app_map: Map
            - responder: Responder
            - path_generation: bool - if True, keeps generating new random paths
                                      to travel if one is completed
    """

    def __init__(self, app_map: Map, responder: Responder, path_generation: bool = True):
        self.__map = app_map
        self.responder = responder

        self._next_move_time: float | None = None
        self._current_move: int | None = None
        self._path: Path | None = None
        self._path_generation = path_generation

        if self._path_generation:
            self._generate_path()

    def _generate_path(self):
        """ Generate a random path to travel """
        while not self._path:
            random_location = Location(
                random.uniform(self.__map.bounding_box[0], self.__map.bounding_box[2]),
                random.uniform(self.__map.bounding_box[1], self.__map.bounding_box[3]))
            if not self.__map.is_valid_location(random_location):
                continue
            self._path = self.__map.get_shortest_path(self.responder.location, random_location)

        self._current_move = 0
        self._next_move_time = 0

    def _handle_move(self):
        """ Handles moving the responder to the next location """
        time_now = time.time()
        self.responder.move(self._path.edges[self._current_move].target.location)
        if self._current_move == len(self._path.edges) - 1:
            if not self._path_generation:
                return
            self._generate_path()
        else:
            self._current_move += 1

        self._next_move_time = time_now + Time(self._path.edges[self._current_move].cost).seconds

    def update(self):
        if self._current_move is None:
            return

        time_now = time.time()
        if time_now >= self._next_move_time:
            self._handle_move()

    def set_path(self, path: Path):
        self._current_move = 0
        self._next_move_time = 0
        self._path = path
