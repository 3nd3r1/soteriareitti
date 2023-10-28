""" soteriareitti/core/station.py """

from enum import Enum

from soteriareitti.core.map import Map, MapPoint

from soteriareitti.classes.geo import Location


class StationType(Enum):
    HOSPITAL = "hospital"
    POLICE_STATION = "police_station"
    FIRE_STATION = "fire_station"


class Station(MapPoint):
    """
    The Station class represents a stationary station that can contain multiple responders. 
    For example: a hospital, a police station or a fire station.

    """

    def __init__(self, app_map: Map, location: Location, station_type: StationType):
        super().__init__(app_map, location, path_algorithm="dijkstra")
        self.type = station_type
        self.id: str = station_type.value + str(id(self))

    def __str__(self):
        return self.id

    def __repr__(self):
        return f"<soteriareitti.Station type={self.type} location={self.location}>"
