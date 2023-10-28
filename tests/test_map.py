""" tests/test_map.py """
import unittest

from soteriareitti.core.map import Map, MapPoint
from soteriareitti.classes.geo import Location
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

    def test_mappoint_ida_star_path_to(self):
        """ Test that the MapPoint finds correct path from MapPoint to MapPoint with ida_star """
        self.map.load_place("Töölö")
        test_point_a = MapPoint(self.map, Location(60.1772996731, 24.9226685992),
                                "ida_star")
        test_point_b = MapPoint(self.map, Location(60.17517934757, 24.91634823927))

        path = test_point_a.path_to(test_point_b)
        self.assertIsNotNone(path)

        path_locations = [node.location for node in path]  # pylint: disable=not-an-iterable

        # pylint: disable-next=protected-access
        start_location = self.map._get_closest_node(test_point_a.location).location
        # pylint: disable-next=protected-access
        end_location = self.map._get_closest_node(test_point_b.location).location

        # Assert that the path starts and ends at correct locations
        self.assertEqual(path_locations[0], start_location)
        self.assertEqual(path_locations[-1], end_location)

    def test_mappoint_dijkstra_path_to(self):
        """ Test that the MapPoint finds correct path from MapPoint to MapPoint with dijkstra """
        self.map.load_place("Töölö")
        test_point_a = MapPoint(self.map, Location(60.1772996731, 24.9226685992),
                                "dijkstra")
        test_point_b = MapPoint(self.map, Location(60.17517934757, 24.91634823927))

        path = test_point_a.path_to(test_point_b)
        self.assertIsNotNone(path)

        path_locations = [node.location for node in path]  # pylint: disable=not-an-iterable

        # pylint: disable-next=protected-access
        start_location = self.map._get_closest_node(test_point_a.location).location
        # pylint: disable-next=protected-access
        end_location = self.map._get_closest_node(test_point_b.location).location

        # Assert that the path starts and ends at correct locations
        self.assertEqual(path_locations[0], start_location)
        self.assertEqual(path_locations[-1], end_location)
