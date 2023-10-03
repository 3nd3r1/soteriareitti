""" tests/test_responder.py """
import unittest

from .helpers import draw

from soteriareitti.core.map import Map
from soteriareitti.core.responder import Responder, ResponderType

from soteriareitti.utils.geo import Location


class TestResponder(unittest.TestCase):
    """ Tests for the Responder class """

    def setUp(self):
        self.map = Map()
        self.map.load_place("Töölö")
        self.ambulance = Responder(self.map, ResponderType.AMBULANCE,
                                   Location(60.1772996731, 24.9226685992))

    def test_station_path_to(self):
        """ Test that the Responder finds correct path from Responder to location """
        test_location = Location(60.17517934757, 24.91634823927)

        path = self.ambulance.path_to(test_location)
        path_locations = [node.location for node in path]

        start_location = self.map.get_closest_node(self.ambulance.location).location
        end_location = self.map.get_closest_node(test_location).location

        # Assert that the path starts and ends at correct locations
        self.assertEqual(path_locations[0], start_location)
        self.assertEqual(path_locations[-1], end_location)
