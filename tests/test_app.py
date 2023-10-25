""" tests/test_app.py """
import unittest

from soteriareitti import SoteriaReitti

from soteriareitti.core.responder import Responder, ResponderType
from soteriareitti.core.station import Station, StationType
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.classes.geo import Location


class TestSoteriaReitti(unittest.TestCase):
    """ Tests for the main class SoteriaReitti """

    def setUp(self):
        self.app = SoteriaReitti()
        self.app.load_place("Töölö")
        self.app.active_emergency = Emergency(
            EmergencyType.FIRE, [ResponderType.AMBULANCE],
            Location(60.1781, 24.9170), "Test emergency")
        self.app.responders = [
            Responder(self.app.map, ResponderType.AMBULANCE, Location(60.1783, 24.9170))]
        self.app.stations = [
            Station(self.app.map, StationType.FIRE_STATION, Location(60.1799, 24.9269))]

    def test_app_constructor(self):
        """ Test the constructor of the SoteriaReitti class """
        self.assertEqual(self.app.map.place, "Töölö")
        self.assertIsNotNone(self.app.active_emergency)
        self.assertEqual(len(self.app.responders), 1)
        self.assertEqual(len(self.app.stations), 1)

    def test_app_clear(self):
        """ Test the clear method """
        self.app.clear()
        self.assertIsNone(self.app.active_emergency)
        self.assertEqual(len(self.app.responders), 0)
        self.assertEqual(len(self.app.stations), 0)

    def test_app_create_emergency(self):
        """ Test the create_emergency method """
        self.app.active_emergency = None

        test_emergency = self.app.create_emergency(EmergencyType.FIRE, [ResponderType.AMBULANCE],
                                                   Location(60.1783, 24.9174), "Test emergency 2")

        self.assertEqual(id(self.app.active_emergency), id(test_emergency))
        self.assertEqual(len(test_emergency.responders), 1)
        self.assertFalse(test_emergency.responders[0].available)

    def test_app_create_responder(self):
        """ Test the create_responder method  """
        test_responder = self.app.create_responder(ResponderType.POLICE_CAR,
                                                   Location(60.1781, 24.9174))
        self.assertEqual(len(self.app.responders), 2)
        self.assertEqual(id(self.app.responders[-1]), id(test_responder))

    def test_app_create_station(self):
        """ Test the create_station method """
        test_station = self.app.create_station(StationType.FIRE_STATION,
                                               Location(60.1781, 24.9174))
        self.assertEqual(len(self.app.stations), 2)
        self.assertEqual(id(self.app.stations[-1]), id(test_station))
