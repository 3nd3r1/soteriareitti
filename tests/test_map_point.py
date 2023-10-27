""" tests/test_map_point.py """

import unittest

from soteriareitti.core.map import Map, MapPoint
from soteriareitti.classes.geo import Location


class TestMapPoint(unittest.TestCase):
    def setUp(self):
        self.map = Map()
        self.map.load_place("Töölö")
        self.test_point_b = MapPoint(self.map, Location(60.17517934757, 24.91634823927))

    def test_mappoint_ida_star_path_to(self):
        """ Test that the MapPoint finds correct path from MapPoint to MapPoint with ida_star """
        test_point_a = MapPoint(self.map, Location(60.1772996731, 24.9226685992),
                                "ida_star")
        test_point_b = self.test_point_b

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
        test_point_a = MapPoint(self.map, Location(60.1772996731, 24.9226685992),
                                "dijkstra")
        test_point_b = self.test_point_b

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
