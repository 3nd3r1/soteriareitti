""" tests/test_emergency.py """

import unittest

from soteriareitti.core.map import Map
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.core.responder import Responder, ResponderType, ResponderStatus
from soteriareitti.core.station import Station, StationType

from soteriareitti.utils.geo import Location


class TestEmergency(unittest.TestCase):
    """ Tests for the Emergency class """

    def setUp(self):
        self.map = Map()
        self.map.load_place("Töölö")
        self.emergency = Emergency(self.map, Location(60.1763691, 24.9142483),
                                   EmergencyType.MEDICAL, [ResponderType.AMBULANCE],
                                   "Test emergency")
        self.responders = [Responder(self.map, Location(60.1767106, 24.9171237),
                                     ResponderType.AMBULANCE),
                           Responder(self.map, Location(60.1775003, 24.9252347),
                                     ResponderType.AMBULANCE),
                           Responder(self.map, Location(60.1837744, 24.9214581),
                                     ResponderType.POLICE_CAR),
                           Responder(self.map, Location(60.1849479, 24.9085835),
                                     ResponderType.FIRE_TRUCK)
                           ]

        self.stations = [Station(self.map, Location(60.1767106, 24.9171237),
                                 StationType.HOSPITAL),
                         Station(self.map, Location(60.1775003, 24.9252347),
                                 StationType.HOSPITAL),
                         Station(self.map, Location(60.1837744, 24.9214581),
                                 StationType.POLICE_STATION)
                         ]

    def test_emergency_creation(self):
        """ Test that the Emergency class is initialized correctly """
        emergency = self.emergency

        self.assertEqual(emergency.type, EmergencyType.MEDICAL)
        # pylint: disable-next=protected-access
        self.assertEqual(emergency._responder_types, [ResponderType.AMBULANCE])
        self.assertEqual(emergency.location, Location(60.1763691, 24.9142483))
        self.assertEqual(emergency.description, "Test emergency")

    def test_emergency_handle(self):
        """ Test that the Emergency is handled correctly """
        emergency = self.emergency

        self.assertEqual(len(emergency.responders), 0)
        emergency.handle(self.responders)

        self.assertEqual(len(emergency.responders), 1)
        self.assertEqual(emergency.responders[0].type, ResponderType.AMBULANCE)
        self.assertEqual(emergency.responders[0].status, ResponderStatus.DISPATCHED)

    def test_emergency_find_best_responder(self):
        """ Test that the Emergency finds correct first responder """
        emergency = self.emergency

        responder = emergency.find_best_responder(self.responders, ResponderType.AMBULANCE)

        self.assertIsNotNone(responder)
        self.assertEqual(responder.type, ResponderType.AMBULANCE)
        self.assertEqual(responder.location,
                         Location(60.1767106, 24.9171237))
