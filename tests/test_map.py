""" tests/test_map.py """
import unittest

from soteriareitti.core.map import Map
from soteriareitti.utils.settings import Settings


class TestMap(unittest.TestCase):
    """ Tests for the Map class """

    def setUp(self):
        self.map = Map()

    def test_map_graph_creation(self):
        """ Tests that the Map creates correct graph """
        # Disable caching
        Settings.caching = False
        self.map.load_place("Töölö")

        self.assertEqual(self.map._place, "Töölö")  # pylint: disable=protected-access
        self.assertEqual(len(self.map._graph.get_nodes()), 3852)  # pylint: disable=protected-access

    def test_map_graph_loading(self):
        """ Tests that the Map loads graph correctly from cache """
        # Enable caching
        Settings.caching = True
        # Create new graph and save it to cache
        Map().load_place("Töölö")

        self.map.load_place("Töölö")
        self.assertEqual(self.map._place, "Töölö")  # pylint: disable=protected-access
        self.assertEqual(len(self.map._graph.get_nodes()), 3852)  # pylint: disable=protected-access
