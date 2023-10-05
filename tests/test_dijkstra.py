""" tests/test_dijkstra.py """
import unittest

from soteriareitti.algorithms.dijkstra import Dijkstra
from soteriareitti.classes.graph import Graph


class TestDijkstra(unittest.TestCase):
    """ Tests for the Dijkstra implementation """

    def setUp(self):
        self.graph = Graph()

        test_edges = [("1", "2", 2), ("2", "3", 1), ("1", "3", 4), ("6", "7", 1),
                      ("7", "8", 1), ("8", "9", 1), ("9", "6", 1)]

        self.graph.add_edges_from(test_edges)

    def test_get_shortest_path(self):
        """
        Test that the Dijkstra implementation finds
        the shortest path correctly in simple graph
        """

        node_source = self.graph.nodes.get("1")
        node_target = self.graph.nodes.get("3")
        shortest_path = Dijkstra.get_shortest_path(self.graph, node_source, node_target)

        self.assertEqual(shortest_path.cost, 3)
        self.assertListEqual([node.id for node in shortest_path], ["1", "2", "3"])
