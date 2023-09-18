""" tests/test_emergency.py """

import unittest

from soteriareitti.core.map import Map
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.core.responder import Responder, ResponderType

from soteriareitti.utils.utils_geo import Location


class TestEmergency(unittest.TestCase):
    """ Tests for the Emergency class """

    def setUp(self):
        self.map = Map("Töölö")
        self.responders = [Responder(self.map, ResponderType.AMBULANCE,
                                     Location(24.9289, 60.1789)),
                           Responder(self.map, ResponderType.AMBULANCE,
                                     Location(24.9265, 60.1825)),
                           Responder(self.map, ResponderType.POLICE_CAR,
                                     Location(24.9188, 60.1812)),
                           Responder(self.map, ResponderType.FIRE_TRUCK,
                                     Location(24.9200, 60.1837))]

    def test_emergency_creation(self):
        """ Test that the Emergency class is initialized correctly """
        emergency = Emergency(EmergencyType.MEDICAL, [ResponderType.AMBULANCE],
                              Location(24.9384, 60.1699), "Test emergency")

        self.assertEqual(emergency.type, EmergencyType.MEDICAL)
        self.assertEqual(emergency.responder_types, [ResponderType.AMBULANCE])
        self.assertEqual(emergency.location, Location(24.9384, 60.1699))
        self.assertEqual(emergency.description, "Test emergency")

    def test_emergency_find_nearest_responder(self):
        """ Test that the Emergency finds correct first responder """
        # One type
        emergency = Emergency(EmergencyType.MEDICAL, [ResponderType.AMBULANCE],
                              Location(24.9230, 60.1846), "Test emergency 1")
        emergency.find_nearest_responders(self.responders)

        self.assertEqual(len(emergency.responders), 1)
        self.assertEqual(emergency.responders[0].type, ResponderType.AMBULANCE)
        self.assertEqual(emergency.responders[0].location,
                         Location(24.9265, 60.1825))

        # Multiple types
        emergency = Emergency(EmergencyType.MEDICAL,
                              [ResponderType.AMBULANCE, ResponderType.POLICE_CAR],
                              Location(24.9129, 60.1799), "Test emergency 2")
        emergency.find_nearest_responders(self.responders)

        self.assertEqual(len(emergency.responders), 2)
        self.assertIn(emergency.responders[0].type, [
                      ResponderType.AMBULANCE, ResponderType.POLICE_CAR])
        self.assertIn(emergency.responders[1].type, [
                      ResponderType.AMBULANCE, ResponderType.POLICE_CAR])
