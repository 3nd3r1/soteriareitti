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

        self.assertEqual(self.map._place, "Töölö")            # pylint: disable=protected-access
        self.assertGreater(len(self.map._graph.get_nodes()),  # pylint: disable=protected-access
                           3800)

    def test_map_graph_loading(self):
        """ Tests that the Map loads graph correctly from cache """
        # Enable caching
        Settings.caching = True

        # Create new graph and save it to cache
        test_map = Map()
        test_map.load_place("Töölö")

        # Load graph from cache
        self.map.load_place("Töölö")
        self.assertEqual(self.map._place, "Töölö")              # pylint: disable=protected-access
        self.assertEqual(len(self.map._graph.get_nodes()),      # pylint: disable=protected-access
                         len(test_map._graph.get_nodes()))      # pylint: disable=protected-access
