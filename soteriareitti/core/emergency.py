""" soteriareitti/core/emergency.py """
import logging
from enum import Enum

from soteriareitti.core.responder import ResponderType, Responder
from soteriareitti.core.station import StationType, Station

from soteriareitti.utils.geo import Location, Distance


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
        logging.debug("Handling emergency: %s", self)
        for responder_type in self.responder_types:
            nearest_responder = self.find_nearest_responder(responders, responder_type)

            # If a responder is available, add it to the emergency
            if nearest_responder:
                nearest_responder.available = False
                self.responders.append(nearest_responder)
                continue

            # If no responders are available, find the nearest stations
            nearest_station = None
            if responder_type == ResponderType.POLICE_CAR:
                nearest_station = self.find_nearest_station(stations, StationType.POLICE_STATION)
            elif responder_type == ResponderType.FIRE_TRUCK:
                nearest_station = self.find_nearest_station(stations, StationType.FIRE_STATION)
            elif responder_type == ResponderType.AMBULANCE:
                nearest_station = self.find_nearest_station(stations, StationType.HOSPITAL)
            else:
                logging.debug("No handler for responder type %s", responder_type)

            if nearest_station:
                self.stations_from.append(nearest_station)
            else:
                logging.debug("No available responders or stations for type %s", responder_type)
                raise ResponderNotFound

    def find_nearest_responder(self, responders: list[Responder],
                               responder_type: ResponderType) -> Responder | None:
        """ Finds the nearest responders of the given type and adds them to the emergency. """
        logging.debug("Finding nearest responders")
        nearest_responder = None
        nearest_distance = Distance(float("inf"))

        for responder in responders:
            if not responder.available or responder.type != responder_type:
                continue

            distance_to_responder = responder.distance_to(self.location)
            if distance_to_responder.meters < nearest_distance.meters:
                nearest_responder = responder
                nearest_distance = distance_to_responder

        if nearest_responder:
            logging.debug("Found nearest responder: %s", nearest_responder)
            return nearest_responder
        logging.debug("No available responders of type %s", responder_type)
        return None

    def find_nearest_station(self, stations: list[Station],
                             station_type: StationType) -> Station | None:
        """ Finds the nearest station of the given type and adds it to the emergency. """
        logging.debug("Finding nearest station")
        nearest_station = None
        nearest_distance = Distance(float("inf"))
        for station in stations:
            if station.type != station_type:
                continue
            distance_to_station = station.distance_to(self.location)
            if distance_to_station.meters < nearest_distance.meters:
                nearest_station = station
                nearest_distance = distance_to_station

        if nearest_station:
            logging.debug("Found nearest station: %s", nearest_station)
            return nearest_station
        logging.debug("No available stations of type %s", station_type)
        return None
