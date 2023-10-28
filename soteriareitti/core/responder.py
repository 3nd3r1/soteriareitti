""" soteriareitti/core/responder.py """
import logging
from enum import Enum

from soteriareitti.core.map import Map, MapPoint
from soteriareitti.core.station import Station

from soteriareitti.classes.geo import Location


class ResponderType(Enum):
    AMBULANCE = "ambulance"
    POLICE_CAR = "police_car"
    FIRE_TRUCK = "fire_truck"


class ResponderStatus(Enum):
    AVAILABLE = "available"
    DISPATCHED = "dispatched"
    ON_SCENE = "on_scene"
    OUT_OF_SERVICE = "out_of_service"


class Responder(MapPoint):
    """
    The `Responder` class represents units that are dispatched to emergency calls.

    For example: an ambulance, fire truck or police car.
    """

    def __init__(self, app_map: Map, location: Location,
                 responder_type: ResponderType, station: Station | None = None):
        super().__init__(app_map, location, path_algorithm="ida_star")

        self.type: ResponderType = responder_type
        self.station: Station | None = station

        self._destination: MapPoint | None = station if station and not self.at_station else None
        self._status: ResponderStatus = ResponderStatus.AVAILABLE

    def __repr__(self) -> str:
        return (f"<soteriareitti.Responder type={self.type} "
                f"location={self.location} status={self.status.value}>")

    def set_status(self, status: ResponderStatus, destination: MapPoint | None = None) -> None:
        """
        Method for changing the responders status and destination

         Args: 
            - status: The status to set the responder to.
            - destination (optional): The MapPoint to dispatch the responder to.
        """
        self._destination = destination
        self._status = status

    def path_to(self, map_point: MapPoint) -> float | None:
        if self.at_station:
            return self.station.path_to(map_point)
        return super().path_to(map_point)

    def cost_to(self, map_point: MapPoint) -> float | None:
        if self.at_station:
            return self.station.cost_to(map_point)
        return super().cost_to(map_point)

    def move(self, location: Location) -> None:
        """ Moves the responder to the given location. """
        logging.debug("Moving responder from %s to %s", self.location, location)
        self.set_location(location)

    @property
    def at_station(self) -> bool:
        """ Returns True if the responder is at a station. """
        if not self.station:
            return False

        return self.location.rounded(3) == self.station.location.rounded(3)

    @property
    def status(self) -> ResponderStatus:
        """ Returns the status of the responder. """
        return self._status

    @property
    def destination(self) -> MapPoint | None:
        """ Returns the destination of the responder. """
        return self._destination
