""" tests/test_responder.py """
import unittest

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

    def test_responder_path_to(self):
        """ Test that the Responder finds correct path from Responder to location """
        test_location = Location(60.17517934757, 24.91634823927)

        path = self.ambulance.path_to(test_location)
        self.assertIsNotNone(path)
        path_locations = [node.location for node in path]  # pylint: disable=not-an-iterable

        start_location = self.map.get_closest_node(self.ambulance.location).location
        end_location = self.map.get_closest_node(test_location).location

        # Assert that the path starts and ends at correct locations
        self.assertEqual(path_locations[0], start_location)
        self.assertEqual(path_locations[-1], end_location)

    def test_responder_move(self):
        """ Tests that the Responder moves correctly """
        self.assertEqual(self.ambulance.location, Location(60.1772996731, 24.9226685992))
        self.ambulance.move(Location(60.23, 24.81))
        self.assertEqual(self.ambulance.location, Location(60.23, 24.81))
