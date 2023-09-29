""" tests/test_station.py """
import unittest

from soteriareitti.core.map import Map
from soteriareitti.core.station import Station, StationType

from soteriareitti.utils.geo import Location


class TestStation(unittest.TestCase):
    """ Tests for the Station class """

    def setUp(self):
        self.map = Map()
        self.map.load_place("Töölö")
        self.station = Station(self.map, StationType.HOSPITAL,
                               Location(60.1772996731, 24.9226685992))

    def test_station_path_from(self):
        """ Test that the Station finds correct path from location to the station """
        test_location = Location(60.17517934757, 24.91634823927)

        points = [Location(60.1751900, 24.9159025), Location(60.1755941, 24.9158538),
                  Location(60.1759172, 24.9183403), Location(60.1765795, 24.9224138),
                  Location(60.1772038, 24.9225399)]

        path = self.station.path_from(test_location)
        path_locations_rounded = [node.location.rounded(4) for node in path]

        # Assert that all points are in the path
        for point in points:
            self.assertIn(point.rounded(4), path_locations_rounded)

        # Distance is approx 500 meters
        self.assertAlmostEqual(path.cost, 500, delta=50)

    def test_station_path_to(self):
        """ Test that the Station finds correct path from station to location """
        test_location = Location(60.17517934757, 24.91634823927)

        points = [Location(60.1772027, 24.9225391), Location(60.1780196, 24.9227350),
                  Location(60.1780776, 24.9248886), Location(60.1774093, 24.9252050),
                  Location(60.1763305, 24.9142083), Location(60.1751886, 24.9159067)]

        path = self.station.path_to(test_location)
        path_locations_rounded = [node.location.rounded(4) for node in path]

        # Assert that all points are in the path
        for point in points:
            self.assertIn(point.rounded(4), path_locations_rounded)

        # Distance is approx 1100 meters
        self.assertAlmostEqual(path.cost, 1100, delta=50)
