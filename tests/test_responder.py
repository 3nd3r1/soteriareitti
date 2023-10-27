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
        self.ambulance = Responder(self.map, Location(
            60.1772996731, 24.9226685992), ResponderType.AMBULANCE)

    def test_responder_move(self):
        """ Tests that the Responder moves correctly """
        self.assertEqual(self.ambulance.location, Location(60.1772996731, 24.9226685992))
        self.ambulance.move(Location(60.178, 24.924))
        self.assertEqual(self.ambulance.location, Location(60.178, 24.924))
