""" soteriareitti/core/station.py """

from enum import Enum

from soteriareitti.core.map import Map

from soteriareitti.classes.graph import Path
from soteriareitti.classes.geo import Location


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

    def __repr__(self):
        return f"<soteriareitti.Station type={self.type} location={self.location}>"

    def path_to(self, location: Location) -> Path:
        """ Return shortest path from station to location """
        path = self.__map.reconstruct_path(self.location, location, self.__dijkstra_data["from"])
        return path.reverse()

    def path_from(self, location: Location) -> Path:
        """ Return shortest path from location to station"""
        path = self.__map.reconstruct_path(self.location, location, self.__dijkstra_data["to"])
        return path

    def cost_to(self, location: Location) -> float:
        """ Get cost to location """
        path = self.path_to(location)
        return path.cost

    def cost_from(self, location: Location) -> float:
        """ Get cost from location """
        path = self.path_from(location)
        return path.cost
