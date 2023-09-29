""" tests/test_emergency.py """

import unittest

from soteriareitti.core.map import Map
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.core.responder import Responder, ResponderType
from soteriareitti.core.station import Station, StationType

from soteriareitti.utils.geo import Location


class TestEmergency(unittest.TestCase):
    """ Tests for the Emergency class """

    def setUp(self):
        self.map = Map("Töölö")
        self.emergency = Emergency(EmergencyType.MEDICAL, [ResponderType.AMBULANCE],
                                   Location(60.1763691, 24.9142483), "Test emergency")
        self.responders = [Responder(self.map, ResponderType.AMBULANCE,
                                     Location(60.1767106, 24.9171237)),
                           Responder(self.map, ResponderType.AMBULANCE,
                                     Location(60.1775003, 24.9252347)),
                           Responder(self.map, ResponderType.POLICE_CAR,
                                     Location(60.1837744, 24.9214581)),
                           Responder(self.map, ResponderType.FIRE_TRUCK,
                                     Location(60.1849479, 24.9085835))]

        self.stations = [Station(self.map, StationType.HOSPITAL, Location(60.1767106, 24.9171237)),
                         Station(self.map, StationType.HOSPITAL, Location(60.1775003, 24.9252347)),
                         Station(self.map, StationType.POLICE_STATION,
                                 Location(60.1837744, 24.9214581))]

    def test_emergency_creation(self):
        """ Test that the Emergency class is initialized correctly """
        emergency = self.emergency

        self.assertEqual(emergency.type, EmergencyType.MEDICAL)
        self.assertEqual(emergency.responder_types, [ResponderType.AMBULANCE])
        self.assertEqual(emergency.location, Location(60.1763691, 24.9142483))
        self.assertEqual(emergency.description, "Test emergency")

    def test_emergency_handle(self):
        """ Test that the Emergency is handled correctly """
        emergency = self.emergency

        self.assertEqual(len(emergency.responders), 0)
        emergency.handle(self.responders, self.stations)

        self.assertEqual(len(emergency.responders), 1)
        self.assertEqual(emergency.responders[0].type, ResponderType.AMBULANCE)
        self.assertEqual(emergency.responders[0].available, False)

    def test_emergency_find_best_responder(self):
        """ Test that the Emergency finds correct first responder """
        emergency = self.emergency

        responder = emergency.find_best_responder(self.responders, ResponderType.AMBULANCE)

        self.assertIsNotNone(responder)
        self.assertEqual(responder.type, ResponderType.AMBULANCE)
        self.assertEqual(responder.location,
                         Location(60.1767106, 24.9171237))

    def test_emergency_find_best_station(self):
        """ Tests that the Emergency finds correct station """
        emergency = self.emergency

        station = emergency.find_best_station(self.stations, StationType.HOSPITAL)

        self.assertIsNotNone(station)
        self.assertEqual(station.type, StationType.HOSPITAL)
        self.assertEqual(station.location, Location(60.1767106, 24.9171237))
