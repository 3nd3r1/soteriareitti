""" tests/test_dijkstra.py """
import unittest

from soteriareitti.algorithms.dijkstra import Dijkstra
from soteriareitti.classes.graph import Graph


class TestDijkstra(unittest.TestCase):
    """ Tests for the Dijkstra implementation """

    def setUp(self):
        self.graph = Graph()

        test_edges = [
            ("1", "2", 2), ("1", "3", 1), ("2", "4", 3), ("2", "5", 2),
            ("3", "6", 1), ("3", "7", 2), ("4", "8", 1), ("5", "9", 4),
            ("6", "10", 3), ("6", "11", 2), ("7", "12", 5), ("8", "13", 2),
            ("9", "14", 1), ("9", "15", 3), ("10", "16", 2), ("11", "17", 4),
            ("12", "18", 3), ("13", "19", 2), ("14", "20", 1), ("15", "21", 5),
            ("16", "22", 2), ("17", "23", 3), ("18", "24", 1), ("19", "25", 4),
            ("20", "26", 3), ("21", "27", 2), ("22", "28", 5), ("23", "29", 1),
            ("24", "30", 2)
        ]

        self.graph.add_edges_from(test_edges)

    def test_dijkstra_finds_small_path(self):
        """ Test that Dijkstra finds a small sized shortest path """
        node_source = self.graph.nodes.get("1")
        node_target = self.graph.nodes.get("12")
        shortest_path = Dijkstra.get_shortest_path(self.graph, node_source, node_target)

        self.assertEqual(shortest_path.cost, 8.0)
        self.assertListEqual([node.id for node in shortest_path], ["1", "3", "7", "12"])

    def test_dijkstra_finds_medium_path(self):
        """ Test that Dijkstra finds a medium sized shortest path """
        node_source = self.graph.nodes.get("2")
        node_target = self.graph.nodes.get("19")
        shortest_path = Dijkstra.get_shortest_path(self.graph, node_source, node_target)

        self.assertEqual(shortest_path.cost, 8.0)
        self.assertListEqual([node.id for node in shortest_path], ["2", "4", "8", "13", "19"])

    def test_dijkstra_finds_large_path(self):
        """ Test that Dijkstra finds a large sized shortest path """
        node_source = self.graph.nodes.get("1")
        node_target = self.graph.nodes.get("27")
        shortest_path = Dijkstra.get_shortest_path(self.graph, node_source, node_target)

        self.assertEqual(shortest_path.cost, 18.0)
        self.assertListEqual([node.id for node in shortest_path], [
                             "1", "2", "5", "9", "15", "21", "27"])
