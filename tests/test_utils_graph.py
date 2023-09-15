""" tests/test_utils_graph.py """

import unittest
from soteriareitti.utils.utils_graph import GraphUtils, Graph


class TestGraph(unittest.TestCase):
    """ Tests for the Graph class and GraphUtils methods """

    def setUp(self):
        self.graph = Graph()

        test_nodes = [("1", 1.0, 1.0), ("2", 2.0, 2.0), ("3", 3.0, 3.0)]
        test_edges = [("1", "2", 2.0), ("2", "3", 1.0), ("1", "3", 4.0)]

        self.graph.add_nodes_from(test_nodes)
        self.graph.add_edges_from(test_edges)

    # Graph tests

    def test_graph_nodes(self):
        """ Test that the graph has the correct nodes """
        self.assertEqual(len(self.graph.get_nodes()), 3)

    def test_graph_edges(self):
        """ Test that the graph has the correct edges """
        self.assertEqual(len(self.graph.get_edges()), 3)

    def test_graph_add_node(self):
        """ Test that the graph adds a node correctly """
        self.assertEqual(len(self.graph.get_nodes()), 3)

        self.graph.add_node(("4", 4.0, 4.0))

        self.assertEqual(len(self.graph.get_nodes()), 4)
        self.assertIn("4", [node.id for node in self.graph.get_nodes()])

    def test_graph_add_edge(self):
        """ Test that the graph adds an edge correctly """
        self.assertEqual(len(self.graph.get_edges()), 3)

        self.graph.add_edge("3", "1", 7.0)

        self.assertEqual(len(self.graph.get_edges()), 4)
        self.assertIn("1", [edge.target.id for edge in self.graph.edges["3"]])
        self.assertIn(7.0, [edge.distance.meters for edge in self.graph.edges["3"]])

    def test_graph_add_invalid_edge(self):
        """ Test that the graph does not add an invalid edge (between nodes that dont exist)"""

        self.assertEqual(len(self.graph.get_edges()), 3)

        self.assertRaises(ValueError, self.graph.add_edge, "1", "4")

        self.assertEqual(len(self.graph.get_edges()), 3)

    def test_graph_add_invalid_node(self):
        """ Test that the graph does not add an invalid node (Wrong type)"""

        self.assertEqual(len(self.graph.get_nodes()), 3)

        self.assertRaises(TypeError, self.graph.add_node, 4)

        self.assertEqual(len(self.graph.get_nodes()), 3)

    # GraphUtils tests

    def test_graph_shortest_path(self):
        """ Test that GraphUtils finds the shortest path correctly """

        node_source = self.graph.nodes.get("1")
        node_target = self.graph.nodes.get("3")
        shortest_path = GraphUtils.dijkstra_shortest_path(self.graph, node_source, node_target)

        print(shortest_path.nodes)

        self.assertEqual(shortest_path.distance.meters, 3.0)
        self.assertListEqual([node.id for node in shortest_path], ["1", "2", "3"])
