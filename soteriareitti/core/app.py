""" soteriareitti/core/app.py """
import logging

from soteriareitti.core.map import Map
from soteriareitti.core.responder import Responder, ResponderType
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.core.station import Station, StationType

from soteriareitti.utils.geo import Location


class SoteriaReitti:
    def __init__(self, place: str):
        self.active_emergency = None

        self._map = Map(place)
        self._responders: list[Responder] = []
        self._stations: list[Station] = []

        logging.debug("SoteriaReitti initialized")

    def create_emergency(self, emergency_type: EmergencyType, responder_types: list[ResponderType],
                         location: Location, description: str):
        """ Creates an emergency call. """

        self.active_emergency = Emergency(emergency_type, responder_types, location, description)
        self.active_emergency.find_nearest_responders(self._responders)

        logging.debug("Created emergency call: %s", self.active_emergency)

    def create_responder(self, responder_type: ResponderType, location: Location):
        """ Creates a first responder """
        new_responder = Responder(self._map, responder_type, location)
        self._responders.append(new_responder)

        logging.debug("Created responder: %s", new_responder)

    def create_station(self, station_type: StationType, location: Location):
        """ Creates a station """
        new_station = Station(self._map, station_type, location)
        self._stations.append(new_station)

        logging.debug("Created station: %s", new_station)
