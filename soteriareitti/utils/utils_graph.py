""" soteriareitti/utils_graph.py """
import logging
import overpy

from utils.utils_geo import Location


class Node:
    def __init__(self, id: str, longitude: float, latitude: float):
        self.id = id
        self.location = Location(longitude, latitude)

    def __repr__(self):
        return "<utils_graph.Node id=%s, location=%s>" % (self.id, self.location)

    @classmethod
    def from_overpy_node(cls, node: overpy.Node):
        if not isinstance(node, overpy.Node):
            raise TypeError(f"Node must be overpy.Node, not {type(node)}")
        if not node.lon or not node.lat:
            raise ValueError(f"Node {node.id} has no longitude or latitude")

        return cls(node.id, float(node.lon), float(node.lat))

    def update(self, node: "Node"):
        """ Update node with data from another node """
        if not isinstance(node, Node):
            raise TypeError(f"Node must be Node, not {type(node)}")

        self.location = node.location


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    @classmethod
    def from_component(cls, component: list[Node]):
        graph = cls()
        graph.add_nodes_from(component)
        graph.add_edges_from(component)
        return graph

    def get_node(self, id: str) -> Node | None:
        """ Get node object by node id"""
        if id in self.nodes:
            return self.nodes[id]
        return None

    def get_nodes(self) -> list[Node]:
        """ Get all nodes """
        return list(self.nodes.values())

    def get_edges(self) -> list[tuple[Node, Node]]:
        """ Get all edges """
        return [(self.nodes[node_a_id], node_b) for node_a_id in self.edges for node_b in self.edges[node_a_id]]

    def add_node(self, node: any):
        """ Add node to graph """

        if isinstance(node, overpy.Node):
            node = Node.from_overpy_node(node)

        if not isinstance(node, Node):
            raise TypeError(f"Node must be overpy.Node or Node, not {type(node)}")

        if node.id not in self.nodes:
            self.edges[node.id] = []
            self.nodes[node.id] = node
        else:
            self.nodes[node.id].update(node)

        return self.nodes[node.id]

    def add_edge(self, node_a: any, node_b: any):
        """ Add edge to graph """
        node_a = self.add_node(node_a)
        node_b = self.add_node(node_b)

        self.edges[node_a.id].append(node_b)

    def add_nodes_from(self, nodes: list[any]):
        """ Add nodes from a list of nodes """
        for node in nodes:
            self.add_node(node)

    def add_edges_from(self, path: list[any]):
        """ Add edges from a path"""
        for edge in list(zip(path[:-1], path[1:])):
            if isinstance(edge[0], overpy.Node):
                if not edge[0].lon or not edge[0].lat:
                    continue

            if isinstance(edge[1], overpy.Node):
                if not edge[1].lon or not edge[1].lat:
                    continue

            self.add_edge(edge[0], edge[1])


class GraphUtils:
    @staticmethod
    def dfs(graph: Graph, node: Node, visited: dict[str]) -> list[Node]:
        """ Depth-first search """
        if visited.get(node.id, False):
            return []

        visited[node.id] = True
        component = [node]

        for neighbour in graph.edges[node.id]:
            component += GraphUtils.dfs(graph, neighbour, visited)

        return component

    @staticmethod
    def get_largest_component(graph: Graph) -> Graph:
        """
        Get subgraph of graph's largest weakly connected component.
        """

        visited = {}
        largest_component = []

        for node in graph.get_nodes():
            new_component = GraphUtils.dfs(graph, node, visited)
            if len(new_component) > len(largest_component):
                largest_component = new_component

        return Graph.from_component(largest_component)
