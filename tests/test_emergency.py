""" tests/test_emergency.py """

import unittest

from soteriareitti.core.map import Map
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.core.responder import Responder, ResponderType

from soteriareitti.utils.geo import Location


class TestEmergency(unittest.TestCase):
    """ Tests for the Emergency class """

    def setUp(self):
        self.map = Map("Töölö")
        self.responders = [Responder(self.map, ResponderType.AMBULANCE,
                                     Location(60.1789, 24.9289)),
                           Responder(self.map, ResponderType.AMBULANCE,
                                     Location(60.1825, 24.9265)),
                           Responder(self.map, ResponderType.POLICE_CAR,
                                     Location(60.1812, 24.9188)),
                           Responder(self.map, ResponderType.FIRE_TRUCK,
                                     Location(60.1837, 24.9200))]

    def test_emergency_creation(self):
        """ Test that the Emergency class is initialized correctly """
        emergency = Emergency(EmergencyType.MEDICAL, [ResponderType.AMBULANCE],
                              Location(60.1699, 24.9384), "Test emergency")

        self.assertEqual(emergency.type, EmergencyType.MEDICAL)
        self.assertEqual(emergency.responder_types, [ResponderType.AMBULANCE])
        self.assertEqual(emergency.location, Location(60.1699, 24.9384))
        self.assertEqual(emergency.description, "Test emergency")

    def test_emergency_find_nearest_responder(self):
        """ Test that the Emergency finds correct first responder """
        # One type
        emergency = Emergency(EmergencyType.MEDICAL, [ResponderType.AMBULANCE],
                              Location(60.1846, 24.9230), "Test emergency 1")
        responder = emergency.find_nearest_responder(self.responders, ResponderType.AMBULANCE)

        self.assertIsNotNone(responder)
        self.assertEqual(responder.type, ResponderType.AMBULANCE)
        self.assertEqual(responder.location,
                         Location(60.1825, 24.9265))
