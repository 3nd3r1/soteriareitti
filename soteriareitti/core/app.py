""" soteriareitti/core/app.py """
import logging

from soteriareitti.core.map import Map
from soteriareitti.core.responder import Responder, ResponderType
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.core.station import Station, StationType

from soteriareitti.classes.geo import Location


class SoteriaReitti:
    def __init__(self):
        self.active_emergency = None

        self._map = Map()
        self._responders: list[Responder] = []
        self._stations: list[Station] = []

        logging.debug("SoteriaReitti initialized")

    def load_place(self, place: str):
        logging.info("Loading place: %s", place)
        self._map.load_place(place)
        logging.info("Loading finished")

    def clear(self):
        self._responders.clear()
        self._stations.clear()
        self.active_emergency = None
        logging.debug("Cleared all app data")

    def create_emergency(self, emergency_type: EmergencyType, responder_types: list[ResponderType],
                         location: Location, description: str) -> Emergency:
        """ Creates an emergency call. """

        self.active_emergency = Emergency(emergency_type, responder_types, location, description)
        self.active_emergency.handle(self._responders, self._stations)

        logging.debug("Created emergency call: %s", self.active_emergency)

        return self.active_emergency

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
