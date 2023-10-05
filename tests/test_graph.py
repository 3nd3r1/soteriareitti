""" tests/test_graph.py """

import unittest

from soteriareitti.classes.graph import Graph
from soteriareitti.utils.graph import GraphUtils


class TestGraph(unittest.TestCase):
    """ Tests for the graph classes and GraphUtils methods """

    def setUp(self):
        self.graph = Graph()

        test_edges = [("1", "2", 2), ("2", "3", 1), ("1", "3", 4), ("6", "7", 1),
                      ("7", "8", 1), ("8", "9", 1), ("9", "6", 1)]

        self.graph.add_edges_from(test_edges)

    # Graph tests

    def test_graph_nodes(self):
        """ Test that the graph has the correct nodes """
        self.assertEqual(len(self.graph.get_nodes()), 7)

    def test_graph_edges(self):
        """ Test that the graph has the correct edges """
        self.assertEqual(len(self.graph.get_edges()), 7)

    def test_graph_add_node(self):
        """ Test that the graph adds a node correctly """
        self.assertEqual(len(self.graph.get_nodes()), 7)
        self.assertNotIn("4", [node.id for node in self.graph.get_nodes()])

        self.graph.add_node("4")

        self.assertEqual(len(self.graph.get_nodes()), 8)
        self.assertIn("4", [node.id for node in self.graph.get_nodes()])

    def test_graph_add_edge(self):
        """ Test that the graph adds an edge correctly """
        self.assertEqual(len(self.graph.get_edges()), 7)
        self.assertNotIn("1", [edge.target.id for edge in self.graph.edges["3"]])
        self.assertNotIn(7, [edge.cost for edge in self.graph.edges["3"]])

        self.graph.add_edge("3", "1", 7)

        self.assertEqual(len(self.graph.get_edges()), 8)
        self.assertIn("1", [edge.target.id for edge in self.graph.edges["3"]])
        self.assertIn(7, [edge.cost for edge in self.graph.edges["3"]])

    # GraphUtils tests

    def test_graph_largest_component(self):
        """ Test that GraphUtils finds the largest component correctly """

        largest_component = GraphUtils.get_largest_component(self.graph)

        self.assertEqual(len(largest_component.get_nodes()), 4)
        self.assertEqual(len(largest_component.get_edges()), 4)

        self.assertListEqual([node.id for node in largest_component.get_nodes()], [
                             "6", "7", "8", "9"])
