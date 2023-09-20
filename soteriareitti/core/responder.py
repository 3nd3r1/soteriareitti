""" soteriareitti/core/responder.py """
from enum import Enum

from soteriareitti.core.map import Map
from soteriareitti.utils.geo import Location
from soteriareitti.utils.graph import Path, Distance


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

    def path_to(self, location: Location) -> Path:
        """ Returns the path to the given location. """
        return self.__map.get_shortest_path(self.location, location)

    def distance_to(self, location: Location) -> Distance:
        """ Returns the distance to the given location. """
        return self.path_to(location).distance
