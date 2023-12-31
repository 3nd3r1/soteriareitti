""" tests/test_app.py """
import unittest

from soteriareitti import SoteriaReitti

from soteriareitti.core.responder import Responder, ResponderType, ResponderStatus
from soteriareitti.core.station import Station, StationType
from soteriareitti.core.emergency import Emergency, EmergencyType
from soteriareitti.classes.geo import Location


class TestSoteriaReitti(unittest.TestCase):
    """ Tests for the main class SoteriaReitti """

    def setUp(self):
        self.app = SoteriaReitti()
        self.app.load_place("Töölö")
        self.app.emergencies = [
            Emergency(self.app.map, Location(60.1781, 24.9170), EmergencyType.FIRE,
                      [ResponderType.AMBULANCE], "Test emergency")]
        self.app.responders = [
            Responder(self.app.map, Location(60.1783, 24.9170), ResponderType.AMBULANCE)]
        self.app.stations = [
            Station(self.app.map, Location(60.1799, 24.9269), StationType.FIRE_STATION)]

    def test_app_constructor(self):
        """ Test the constructor of the SoteriaReitti class """
        self.assertEqual(self.app.map.place, "Töölö")
        self.assertEqual(len(self.app.emergencies), 1)
        self.assertEqual(len(self.app.responders), 1)
        self.assertEqual(len(self.app.stations), 1)

    def test_app_clear(self):
        """ Test the clear method """
        self.app.clear()
        self.assertEqual(len(self.app.emergencies), 0)
        self.assertEqual(len(self.app.responders), 0)
        self.assertEqual(len(self.app.stations), 0)

    def test_app_create_emergency(self):
        """ Test the create_emergency method """
        test_emergency = self.app.create_emergency(EmergencyType.FIRE, [ResponderType.AMBULANCE],
                                                   Location(60.1783, 24.9174), "Test emergency 2")

        self.assertEqual(len(self.app.emergencies), 2)
        self.assertEqual(id(self.app.emergencies[-1]), id(test_emergency))
        self.assertEqual(len(test_emergency.responders), 1)
        self.assertEqual(test_emergency.responders[0].status, ResponderStatus.DISPATCHED)

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
