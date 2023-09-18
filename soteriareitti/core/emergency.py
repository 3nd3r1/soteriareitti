""" soteriareitti/core/emergency.py """

from enum import Enum

from soteriareitti.core.map import Map
from soteriareitti.core.responder import ResponderType, Responder

from soteriareitti.utils.utils_geo import Location, Distance


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
        self.responder_types = responder_types
        self.location = location
        self.description = description

        self.responders = []

    def __str__(self):
        return f"Emergency: {self.type}, {self.location}, {self.description}"

    def find_nearest_responders(self, responders: list[Responder]):
        for responder_type in self.responder_types:
            nearest_responder = None
            nearest_distance = Distance(float("inf"))

            for responder in responders:
                if not responder.available or responder.type != responder_type:
                    continue

                distance_to_responder = responder.distance_to(self.location)
                if distance_to_responder.meters < nearest_distance.meters:
                    nearest_responder = responder
                    nearest_distance = distance_to_responder

            nearest_responder.available = False
            self.responders.append(nearest_responder)
