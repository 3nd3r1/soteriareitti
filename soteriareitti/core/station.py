""" soteriareitti/core/station.py """

from enum import Enum

from soteriareitti.core.map import Map
from soteriareitti.utils.graph import Path
from soteriareitti.utils.geo import Location, Distance


class StationType(Enum):
    HOSPITAL = "hospital"
    POLICE_STATION = "police_station"
    FIRE_STATION = "fire_station"


class Station:
    """
    The Station class represents a fixed station utilized
    for transporting clients to or responders from their respective destinations.

    For example: a hospital, a police station or a fire station.

    The attribute `__dijkstra_data` is used for storing data
    that contains the shortest path from all nodes the station's location.
    """

    def __init__(self, app_map: Map,  station_type: StationType, location: Location):
        self.type = station_type
        self.location = location

        self.__map = app_map
        self.__dijkstra_data = self.__map.get_dijkstra_data(self.location)

    def __str__(self):
        return f"{self.type} station at {self.location}"

    def path_to(self, location: Location) -> Path:
        """ Return shortest path from station to location """
        path = self.__map.reconstruct_path(self.location, location, self.__dijkstra_data["from"])
        return path.reverse()

    def path_from(self, location: Location) -> Path:
        """ Return shortest path from location to station"""
        path = self.__map.reconstruct_path(self.location, location, self.__dijkstra_data["to"])
        return path

    def distance_to(self, location: Location) -> Distance:
        """ Get distance to location """
        path = self.path_to(location)
        return path.distance

    def distance_from(self, location: Location) -> Distance:
        """ Get distance from location """
        path = self.path_from(location)
        return path.distance
