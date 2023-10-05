""" tests/test_ida_star.py """
import unittest

from soteriareitti.algorithms.ida_star import IdaStar
from soteriareitti.classes.graph import Graph


class TestIdaStar(unittest.TestCase):
    """ Tests for the IDA* implementation """

    def setUp(self):
        self.graph = Graph()

        self.graph.add_node("1", pos=(0, 0))
        self.graph.add_node("2", pos=(2, 0))
        self.graph.add_node("3", pos=(3, 1))
        self.graph.add_node("4", pos=(2, -1))
        self.graph.add_node("5", pos=(4, -1))
        self.graph.add_node("6", pos=(4, 0))
        self.graph.add_node("7", pos=(4, 2))

        test_edges = [("1", "2"), ("2", "3"), ("1", "3"), ("2", "3"), ("2", "4"),
                      ("2", "6"), ("3", "7"), ("4", "5"), ("5", "6"), ("6", "7")]

        for edge in test_edges:
            pos1 = self.graph.nodes.get(edge[0]).pos
            pos2 = self.graph.nodes.get(edge[1]).pos
            cost = ((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)**0.5

            self.graph.add_edge(edge[0], edge[1], cost)

    def test_get_shortest_path(self):
        """
        Test that the IDA* implementation finds
        the shortest path correctly in simple graph

        And using euclidean distance as heuristic
        """
        def euclidean_distance(node_a, node_b) -> float:
            """ Euclidean distance between two nodes """
            return float((node_a.pos[0]-node_b.pos[0])**2 + (node_a.pos[1]-node_b.pos[1])**2)**0.5

        node_source = self.graph.nodes.get("1")
        node_target = self.graph.nodes.get("7")

        shortest_path = IdaStar.get_shortest_path(
            self.graph, euclidean_distance, node_source, node_target)

        self.assertAlmostEqual(shortest_path.cost, 4.58, places=2)
        self.assertListEqual([node.id for node in shortest_path], ["1", "3", "7"])
