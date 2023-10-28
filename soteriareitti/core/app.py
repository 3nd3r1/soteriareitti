""" soteriareitti/core/app.py """
import logging

from soteriareitti.core.map import Map
from soteriareitti.core.responder import Responder, ResponderType
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.core.station import Station, StationType

from soteriareitti.classes.geo import Location


class SoteriaReitti:
    def __init__(self):
        self.map = Map()

        self.emergencies: list[Emergency] = []
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
        self.emergencies.clear()
        logging.debug("Cleared all app data")

    def create_emergency(self, emergency_type: EmergencyType, responder_types: list[ResponderType],
                         location: Location, description: str) -> Emergency:
        """ Creates an emergency call. """

        new_emergency = Emergency(self.map, location, emergency_type, responder_types, description)
        new_emergency.handle(self.responders)
        self.emergencies.append(new_emergency)

        logging.debug("Created emergency call: %s", new_emergency)
        return new_emergency

    def create_responder(self, responder_type: ResponderType,
                         location: Location, station: Station | None = None) -> Responder:
        """ Creates a responder """

        new_responder = Responder(self.map, location, responder_type, station)
        self.responders.append(new_responder)

        logging.debug("Created responder: %s", new_responder)
        return new_responder

    def create_station(self, station_type: StationType, location: Location) -> Station:
        """ Creates a station """

        new_station = Station(self.map, location, station_type)
        self.stations.append(new_station)

        logging.debug("Created station: %s", new_station)
        return new_station
