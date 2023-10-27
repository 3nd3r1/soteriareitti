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
