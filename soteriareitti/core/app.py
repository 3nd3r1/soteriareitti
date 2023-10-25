""" soteriareitti/core/app.py """
import logging

from soteriareitti.core.map import Map, InvalidLocation
from soteriareitti.core.responder import Responder, ResponderType
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.core.station import Station, StationType

from soteriareitti.classes.geo import Location


class SoteriaReitti:
    def __init__(self):
        self.map = Map()

        self.active_emergency = None
        self.responders: list[Responder] = []
        self.stations: list[Station] = []

        logging.debug("SoteriaReitti initialized")

    def load_place(self, place: str):
        logging.info("Loading place: %s", place)
        self.map.load_place(place)
        logging.info("Loading finished")

    def clear(self):
        self.responders.clear()
        self.stations.clear()
        self.active_emergency = None
        logging.debug("Cleared all app data")

    def create_emergency(self, emergency_type: EmergencyType, responder_types: list[ResponderType],
                         location: Location, description: str) -> Emergency:
        """ Creates an emergency call. """

        if not self.map.is_valid_location(location):
            logging.error("Invalid location: %s", location)
            raise InvalidLocation

        self.active_emergency = Emergency(emergency_type, responder_types, location, description)
        self.active_emergency.handle(self.responders, self.stations)

        logging.debug("Created emergency call: %s", self.active_emergency)
        return self.active_emergency

    def create_responder(self, responder_type: ResponderType, location: Location) -> Responder:
        """ Creates a first responder """

        if not self.map.is_valid_location(location):
            logging.error("Invalid location: %s", location)
            raise InvalidLocation

        new_responder = Responder(self.map, responder_type, location)
        self.responders.append(new_responder)

        logging.debug("Created responder: %s", new_responder)
        return new_responder

    def create_station(self, station_type: StationType, location: Location) -> Station:
        """ Creates a station """

        if not self.map.is_valid_location(location):
            logging.error("Invalid location: %s", location)
            raise InvalidLocation

        new_station = Station(self.map, station_type, location)
        self.stations.append(new_station)

        logging.debug("Created station: %s", new_station)
        return new_station
