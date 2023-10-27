""" tests/test_simulation.py """

import unittest

from soteriareitti.core.map import Map, MapPoint
from soteriareitti.core.responder import Responder, ResponderType, ResponderStatus

from soteriareitti.classes.geo import Location

from soteriareitti.utils.simulation import ResponderSimulator


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.map = Map()
        self.map.load_place("Töölö")
        self.responder = Responder(self.map, Location(60.175176, 24.923655),
                                   ResponderType.AMBULANCE)

    def test_simulation_moves_responder(self):
        self.responder.set_status(ResponderStatus.DISPATCHED,
                                  MapPoint(self.map, Location(60.1751729, 24.9237073)))
        test_simulation = ResponderSimulator(self.responder, False)

        # Simulate responders 200 times and disable the time delay
        for _ in range(200):
            test_simulation.update()
            test_simulation._next_move_time = 0  # pylint: disable=protected-access

        # Assert that the responder has moved to the correct location
        self.assertEqual(self.responder.location, Location(60.1751729, 24.9237073))
