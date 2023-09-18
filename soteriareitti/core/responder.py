""" soteriareitti/core/responder.py """
from enum import Enum

from soteriareitti.core.map import Map
from soteriareitti.utils.utils_geo import GeoUtils, Location, Distance


class ResponderType(Enum):
    AMBULANCE = "ambulance"
    POLICE_CAR = "police_car"
    FIRE_TRUCK = "fire_truck"


class Responder:
    """
    Responder class represents first responder vehicle that is used to respond to emergency calls.

    Responder can be an ambulance, fire truck or police car.
    """

    def __init__(self, app_map: Map, responder_type: ResponderType, location: Location):
        self.__map = app_map
        self.type = responder_type
        self.location = location

        self.available = True

    def distance_to(self, location: Location) -> Distance:
        """ Return responders distance to given location """

        node_source = self.__map.get_closest_node(self.location)
        node_target = self.__map.get_closest_node(location)

        path = self.__map.get_shortest_path(node_source, node_target)

        return path.distance
