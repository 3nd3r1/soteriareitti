""" soteriareitti/utils/simulation.py """
import time
import random

from soteriareitti.core.map import MapPoint, InvalidLocation
from soteriareitti.core.responder import Responder, ResponderStatus

from soteriareitti.classes.geo import Time, Location
from soteriareitti.classes.graph import Path


class ResponderSimulator:
    """
      This class is used to simulate a single responder's movement

        args:
            - responder: Responder
            - patrolling: bool - if True, keeps generating new random paths
                                      to travel if one is completed
    """

    def __init__(self, responder: Responder, patrolling: bool = False):
        self.responder = responder

        self._next_move_time: float | None = None
        self._current_move: int | None = None
        self._path: Path | None = None
        self._destination: MapPoint | None = None

        self._patrolling = patrolling

        if self._patrolling:
            self._generate_path()

    def _generate_path(self):
        """ Generate a random path to travel """
        while not self._path:
            responder_map = self.responder.map
            while True:
                try:
                    random_location = Location(
                        random.uniform(responder_map.bounding_box[0],
                                       responder_map.bounding_box[2]),
                        random.uniform(responder_map.bounding_box[1],
                                       responder_map.bounding_box[3]))
                    self._destination = MapPoint(responder_map, random_location, "ida_star")
                    break
                except InvalidLocation:
                    pass
            self._path = self.responder.path_to(self._destination)

        self._current_move = 0
        self._next_move_time = 0

    def _handle_move(self):
        """ Handles moving the responder to the next location """
        time_now = time.time()
        self.responder.move(self._path.edges[self._current_move].target.location)
        if self._current_move == len(self._path.edges) - 1:
            if self.responder.status == ResponderStatus.DISPATCHED:
                # If responder has been sent to emergency
                self.responder.set_status(ResponderStatus.ON_SCENE, None)
                self._next_move_time = time_now + 30
            elif (self.responder.status == ResponderStatus.ON_SCENE and
                  not self._patrolling and self.responder.station):
                # If responder has been on scene for 30 seconds
                self.responder.set_status(ResponderStatus.AVAILABLE, self.responder.station)
            elif self._patrolling:
                # If responder is patrolling
                self._generate_path()
            else:
                self._destination = None
                self._current_move = None
                self._path = None
                self.responder.set_status(ResponderStatus.AVAILABLE, None)
            return

        self._current_move += 1
        self._next_move_time = time_now + Time(self._path.edges[self._current_move].cost).seconds

    def update(self):
        if self.responder.destination and self._destination != self.responder.destination:
            self._destination = self.responder.destination
            self._path = self.responder.path_to(self._destination)
            self._current_move = 0
            self._next_move_time = 0

        if self._current_move is None:
            return

        time_now = time.time()
        if time_now >= self._next_move_time:
            self._handle_move()
