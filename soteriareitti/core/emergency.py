""" soteriareitti/core/emergency.py """
import logging
from enum import Enum

from soteriareitti.core.responder import ResponderType, Responder
from soteriareitti.core.station import StationType, Station

from soteriareitti.classes.geo import Location


class ResponderNotFound(Exception):
    """ Raised when a responder couldn't be found for emergency. """


class EmergencyType(Enum):
    """ Enum that represents the type of the emergency. """

    TRAFFIC_ACCIDENT = "traffic_accident"
    MEDICAL = "medical"
    FIRE = "fire"
    CRIME = "crime"
    OTHER = "other"


class Emergency:
    """ Class that represents an emergency call. """

    def __init__(self, emergency_type: EmergencyType,
                 responder_types: list[ResponderType], location: Location, description: str):
        self.type = emergency_type
        self.location = location
        self.description = description

        self.responder_types = responder_types

        self.responders: list[Responder] = []  # Responders currently navigating to the emergency
        self.stations_from: list[Station] = []  # Stations that are currently being navigated from
        self.stations_to: list[Station] = []  # Stations that are currently being navigated to

    def __repr__(self):
        return (f"<soteriareitti.Emergency type={self.type},"
                f"location={self.location}, desc={self.description}>")

    def __del__(self):
        for responder in self.responders:
            responder.available = True
        del self

    def handle(self, responders: list[Responder], stations: list[Station]):
        """ Handles the emergency. """
        logging.info("Handling emergency: %s", self)
        for responder_type in self.responder_types:
            best_responder = self.find_best_responder(responders, responder_type)

            # If a responder is available, add it to the emergency
            if best_responder:
                best_responder.available = False
                self.responders.append(best_responder)
                continue

            # If no responders are available, find the best station
            best_station = None
            if responder_type == ResponderType.POLICE_CAR:
                best_station = self.find_best_station(stations, StationType.POLICE_STATION)
            elif responder_type == ResponderType.FIRE_TRUCK:
                best_station = self.find_best_station(stations, StationType.FIRE_STATION)
            elif responder_type == ResponderType.AMBULANCE:
                best_station = self.find_best_station(stations, StationType.HOSPITAL)
            else:
                logging.debug("No handler for responder type %s", responder_type)

            if best_station:
                self.stations_from.append(best_station)
            else:
                logging.error("No available responders or stations for type %s", responder_type)
                raise ResponderNotFound
        logging.info("Emergency handled.")

    def find_best_responder(self, responders: list[Responder],
                            responder_type: ResponderType) -> Responder | None:
        """ Finds the lowest cost responder of the given type. """
        logging.debug("Finding lowest cost responder to emergency %s", self)
        best_responder = None
        min_cost = float("inf")

        for responder in responders:
            if not responder.available or responder.type != responder_type:
                continue

            cost_responder = responder.cost_to(self.location)
            if cost_responder and cost_responder < min_cost:
                best_responder = responder
                min_cost = cost_responder

        if best_responder:
            logging.debug("Found best responder: %s", best_responder)
            return best_responder
        logging.debug("No available responders of type %s", responder_type)
        return None

    def find_best_station(self, stations: list[Station],
                          station_type: StationType) -> Station | None:
        """ Finds the lowest cost station of the given type . """
        logging.debug("Finding lowest cost station to emergency %s", self)
        best_station = None
        min_cost = float("inf")
        for station in stations:
            if station.type != station_type:
                continue
            cost_station = station.cost_to(self.location)
            if cost_station < min_cost:
                min_cost = cost_station
                best_station = station

        if best_station:
            logging.debug("Found best station: %s", best_station)
            return best_station
        logging.debug("No available stations of type %s", station_type)
        return None
