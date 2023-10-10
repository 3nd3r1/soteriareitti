""" soteriareitti/core/responder.py """
import logging
from enum import Enum

from soteriareitti.core.map import Map

from soteriareitti.classes.geo import Location
from soteriareitti.classes.graph import Path


class ResponderType(Enum):
    AMBULANCE = "ambulance"
    POLICE_CAR = "police_car"
    FIRE_TRUCK = "fire_truck"


class Responder:
    """
    The `Responder` class represents first responders that area used to respond to emergency calls.

    For example: an ambulance, fire truck or police car.
    """

    def __init__(self, app_map: Map, responder_type: ResponderType, location: Location):
        self.__map = app_map

        self.type = responder_type
        self.location = location
        self.available = True

        # Store the last path to avoid recalculating it
        self.__last_path: list[Location | None, Path | None] = [None, None]

    def __repr__(self) -> str:
        return (f"<soteriareitti.Responder type={self.type} "
                f"location={self.location} available={self.available}>")

    def path_to(self, location: Location) -> Path | None:
        """ Returns the path to the given location. """
        if self.__last_path[0] != location:
            logging.debug("Calculating path from %s to %s", self.location, location)
            self.__last_path[0] = location
            self.__last_path[1] = self.__map.get_shortest_path(self.location, location)
        else:
            logging.debug("Using stored path from %s to %s", self.location, location)

        return self.__last_path[1]

    def cost_to(self, location: Location) -> float | None:
        """ Returns the distance to the given location. """
        path_to = self.path_to(location)
        if not path_to:
            return None

        return path_to.cost

    def move(self, location: Location) -> None:
        """ Moves the responder to the given location. """
        logging.debug("Moving responder from %s to %s", self.location, location)
        self.location = location
        self.__last_path = [None, None]
