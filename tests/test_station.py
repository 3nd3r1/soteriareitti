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

        path = self.station.path_from(test_location)
        path_locations = [node.location for node in path]

        start_location = self.map.get_closest_node(test_location).location
        end_location = self.map.get_closest_node(self.station.location).location

        # Assert that the path starts and ends at correct locations
        self.assertEqual(path_locations[0], start_location)
        self.assertEqual(path_locations[-1], end_location)

    def test_station_path_to(self):
        """ Test that the Station finds correct path from station to location """
        test_location = Location(60.17517934757, 24.91634823927)

        path = self.station.path_to(test_location)
        path_locations = [node.location for node in path]

        start_location = self.map.get_closest_node(self.station.location).location
        end_location = self.map.get_closest_node(test_location).location

        # Assert that the path starts and ends at correct locations
        self.assertEqual(path_locations[0], start_location)
        self.assertEqual(path_locations[-1], end_location)
