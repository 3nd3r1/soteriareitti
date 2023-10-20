""" tests/test_simulation.py """

import unittest
import time

from soteriareitti.core.map import Map
from soteriareitti.core.responder import Responder, ResponderType

from soteriareitti.classes.geo import Location

from soteriareitti.utils.simulation import ResponderSimulator


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.map = Map()
        self.map.load_place("Töölö")
        self.responder = Responder(self.map, ResponderType.AMBULANCE,
                                   Location(60.175176, 24.923655))

    def test_simulation_moves_responder(self):
        test_simulation = ResponderSimulator(self.map, self.responder, False)
        test_simulation.set_path(self.responder.path_to(Location(60.1751729, 24.9237073)))

        # Simulate responders 200 times and disable the time delay
        for _ in range(200):
            test_simulation._next_move_time = 0  # pylint: disable=protected-access
            test_simulation.update()

        # Assert that the responder has moved to the correct location
        self.assertEqual(self.responder.location, Location(60.1751729, 24.9237073))
