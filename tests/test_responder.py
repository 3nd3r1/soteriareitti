""" tests/test_responder.py """
import unittest

from soteriareitti.core.map import Map
from soteriareitti.core.responder import Responder, ResponderType

from soteriareitti.utils.geo import Location


class TestResponder(unittest.TestCase):
    """ Tests for the Responder class """

    def setUp(self):
        self.map = Map("Töölö")
        self.ambulance = Responder(self.map, ResponderType.AMBULANCE,
                                   Location(60.1772996731, 24.9226685992))

    def test_station_path_to(self):
        """ Test that the Responder finds correct path from Responder to location """
        test_location = Location(60.17517934757, 24.91634823927)

        points = [Location(60.1772027, 24.9225391), Location(60.1780196, 24.9227350),
                  Location(60.1780776, 24.9248886), Location(60.1774093, 24.9252050),
                  Location(60.1763305, 24.9142083), Location(60.1751886, 24.9159067)]

        path = self.ambulance.path_to(test_location)
        path_locations_rounded = [node.location.rounded(4) for node in path]

        # Assert that all points are in the path
        for point in points:
            self.assertIn(point.rounded(4), path_locations_rounded)

        # Distance is approx 1100 meters
        self.assertAlmostEqual(path.cost, 1100, delta=50)
