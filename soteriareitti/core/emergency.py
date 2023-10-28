""" soteriareitti/core/emergency.py """
import logging
from enum import Enum

from soteriareitti.core.map import MapPoint, Map
from soteriareitti.core.responder import ResponderType, ResponderStatus, Responder

from soteriareitti.classes.geo import Location


class ResponderNotFound(Exception):
    """ Raised when a responder couldn't be found for emergency. """


class EmergencyType(Enum):
    TRAFFIC_ACCIDENT = "traffic_accident"
    MEDICAL = "medical"
    FIRE = "fire"
    CRIME = "crime"
    OTHER = "other"


class Emergency(MapPoint):
    """ Class that represents an emergency call. """

    def __init__(self, app_map: Map, location: Location, emergency_type: EmergencyType,
                 responder_types: list[ResponderType], description: str):
        super().__init__(app_map, location, path_algorithm="ida_star")
        self.type = emergency_type
        self.description = description

        self._responder_types = responder_types
        self._responders: list[Responder] = []  # Responders currently navigating to the emergency

    def __repr__(self):
        return (f"<soteriareitti.Emergency type={self.type},"
                f"location={self.location}, desc={self.description}>")

    def __del__(self):
        for responder in self.responders:
            responder.set_status(ResponderStatus.AVAILABLE, None)
        del self

    def handle(self, responders: list[Responder]):
        """ Handles the emergency. """

        logging.info("Handling emergency: %s", self)
        for responder_type in self._responder_types:
            best_responder = self.find_best_responder(responders, responder_type)

            # If a responder is available, add it to the emergency
            if best_responder:
                best_responder.set_status(ResponderStatus.DISPATCHED, self)
                self.responders.append(best_responder)
                continue

            raise ResponderNotFound

        logging.info("Emergency handled.")

    def find_best_responder(self, responders: list[Responder],
                            responder_type: ResponderType) -> Responder | None:
        """ Finds the lowest cost responder of the given type. """
        logging.debug("Finding lowest cost responder to emergency %s", self)
        best_responder = None
        min_cost = float("inf")

        for responder in responders:
            if responder.status != ResponderStatus.AVAILABLE or responder.type != responder_type:
                continue

            cost_responder = responder.cost_to(self)
            if cost_responder and cost_responder < min_cost:
                best_responder = responder
                min_cost = cost_responder

        if best_responder:
            logging.debug("Found best responder: %s", best_responder)
            return best_responder
        return None

    @property
    def responders(self) -> list[Responder]:
        return self._responders
