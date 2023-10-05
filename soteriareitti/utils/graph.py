""" soteriareitti/utils/graph.py """
from typing import Any
from soteriareitti.classes.graph import Graph, Node, Edge, Path


class GraphUtils:
    @staticmethod
    def reconstruct_path(previous: dict[Any, Edge], source: Node, target: Node) -> Path | None:
        """ Reconstruct path from `previous` dictionary """

        current_edge = previous.get(target.id)
        path = Path.from_nodes([target])

        while current_edge:
            path.add_node(current_edge.source, current_edge.cost)
            if current_edge.source.id == source.id:
                return path
            current_edge = previous.get(current_edge.source.id)

        return None

    @staticmethod
    def reverse_graph(graph: Graph) -> Graph:
        """ Reverse all edges in a directional graph """
        edges = graph.get_edges()
        reversed_edges = [Edge(edge.target, edge.source, edge.cost) for edge in edges]

        new_graph = Graph()
        new_graph.add_nodes_from(graph.get_nodes())
        new_graph.add_edges_from(reversed_edges)

        return new_graph

    @staticmethod
    def get_largest_component(graph: Graph) -> Graph:
        """ Get largest component from graph """

        visited = {}
        largest_component = []

        for node in graph.get_nodes():
            if visited.get(node.id, False):
                continue
            component = []
            stack = [node]

            while stack:
                current_node = stack.pop()

                if visited.get(current_node.id, False):
                    continue

                component.append(current_node)
                visited[current_node.id] = True

                for edge in graph.edges[current_node.id]:
                    stack.append(edge.target)

            if len(component) > len(largest_component):
                largest_component = component

        # Create new graph from largest component
        new_graph = Graph()

        new_graph.add_nodes_from(largest_component)
        for edge in graph.get_edges():
            if edge.source.id in new_graph.nodes and edge.target.id in new_graph.nodes:
                new_graph.add_edge(edge.source, edge.target, edge.cost)

        return new_graph
