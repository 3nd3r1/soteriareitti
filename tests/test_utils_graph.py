""" tests/test_utils_graph.py """

import unittest
from soteriareitti.utils.utils_graph import Graph


class TestGraph(unittest.TestCase):
    """ Tests for the Graph class and GraphUtils methods """

    def setUp(self):
        self.graph = Graph()

        test_nodes = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
        test_edges = [(1, 2, 1), (2, 3, 1), (3, 1, 1)]

        self.graph.add_nodes_from(test_nodes)
        self.graph.add_edges_from(test_edges)

    def test_graph_nodes(self):
        """ Test that the graph has the correct nodes """
        self.assertEqual(len(self.graph.nodes), 3)

    def test_graph_edges(self):
        """ Test that the graph has the correct edges """
        self.assertEqual(len(self.graph.edges), 3)

    def test_graph_add_node(self):
        """ Test that the graph adds a node correctly """
        self.assertEqual(len(self.graph.nodes), 3)

        self.graph.add_node((4, 4, 4))

        self.assertEqual(len(self.graph.nodes), 4)
        self.assertIn(4, [node.id for node in self.graph.get_nodes()])

    def test_graph_add_edge(self):
        """ Test that the graph adds an edge correctly """
        self.assertEqual(len(self.graph.edges), 3)

        self.graph.add_edge(1, 3, 3)

        self.assertEqual(len(self.graph.edges), 4)
        self.assertIn(3, [node.id for node in self.graph.edges[1]])

    def test_graph_add_invalid_edge(self):
        """ Test that the graph does not add an invalid edge (between nodes that dont exist)"""

        self.assertEqual(len(self.graph.edges), 3)

        self.assertRaises(ValueError, self.graph.add_edge, 1, 4, 4)

        self.assertEqual(len(self.graph.edges), 3)

    def test_graph_add_invalid_node(self):
        """ Test that the graph does not add an invalid node (Wrong type)"""

        self.assertEqual(len(self.graph.nodes), 3)

        self.assertRaises(ValueError, self.graph.add_node, (1, 1, 1))

        self.assertEqual(len(self.graph.nodes), 3)
