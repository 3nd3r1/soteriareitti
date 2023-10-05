""" soteriareitti/classes/graph.py """
from typing import Any


class Node:
    """ Node class that represents a node in a graph """

    def __init__(self, node_id: str, **kwargs):
        if not isinstance(node_id, str):
            raise TypeError(f"Node_id must be str, not {type(node_id)}")
        self.id = node_id
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        return self.id

    def __repr__(self):
        return f"<soteriareitti.Node id={self.id}>"

    def update(self, node: "Node" or None = None, **kwargs):
        """ Update node with data from another node """
        if node:
            if not isinstance(node, Node):
                raise TypeError(f"Node must be Node, not {type(node)}")
            self.__dict__.update(node.__dict__)
        self.__dict__.update(kwargs)


class Edge:
    """ 
    Edge class that represents an edge between two nodes

    - source and target must be nodes in the graph
    - cost must be convertible to float
    """

    def __init__(self, source: Node, target: Node, cost: float | int | str):
        if not isinstance(source, Node) or not isinstance(target, Node):
            raise TypeError(
                f"Source and target must be Node, not {type(source)} and {type(target)}")

        if not isinstance(cost, (float, int, str)):
            raise TypeError(f"Cost must be float, int or str, not {type(cost)}")

        self.source: Node = source
        self.target: Node = target
        self.cost: float = float(cost)

    def __repr__(self):
        return (f"<soteriareitti.Edge source={self.source},"
                f"target={self.target}, cost={self.cost}>")


class Path:
    """ Path class that represents a path between multiple nodes """

    def __init__(self, edges: list[Edge] | None = None):
        self.cost: float = 0.0
        self.__visited = {}

        if edges:
            for edge in edges:
                if not isinstance(edge, Edge):
                    raise TypeError(f"Edge must be Edge, not {type(edge)}")
                self.cost += edge.cost
                self.__visited[edge.target] = True
            self.__edges = edges
        else:
            self.__edges = []

    @classmethod
    def from_nodes(cls, nodes: list[Node]):
        path = cls()
        for node in nodes:
            path.add_node(node)
        return path

    def __repr__(self):
        return f"<soteriareitti.Path nodes={len(self)}, cost={self.cost}>"

    def __iter__(self):
        for edge in self.__edges:
            yield edge.target

    def __len__(self):
        return len(self.__edges)

    def add_node(self, node: Node, cost: float | int | str = 0):
        """
        Add node to path 
        """
        self.__visited[node.id] = True
        if self.last:
            new_edge = Edge(self.last, node, cost)
            self.__edges.append(new_edge)
            self.cost += new_edge.cost
        else:
            self.__edges.append(Edge(node, node, cost))

    def pop(self) -> Node:
        self.cost -= self.__edges[-1].cost
        self.__visited[self.last.id] = False
        return self.__edges.pop().target

    def reverse(self) -> "Path":
        return Path(self.__edges[::-1])

    def contains(self, node: Node) -> bool:
        return self.__visited.get(node.id, False)

    @property
    def last(self) -> Node | None:
        if len(self.__edges) > 0:
            return self.__edges[-1].target
        return None


class Graph:
    # Store a version so cache is cleared if version changes
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.edges: dict[str, Edge] = {}

    def __repr__(self) -> str:
        return f"<soteriareitti.Graph nodes={len(self.get_nodes())}, edges={len(self.get_edges())}>"

    def get_nodes(self) -> list[Node]:
        """ Get all nodes """
        return list(self.nodes.values())

    def get_edges(self) -> list[Edge]:
        """ Get all edges """
        edges = []
        for edge_list in self.edges.values():
            edges += edge_list
        return edges

    def add_node(self, node: str | Node, **kwargs) -> Node:
        """
         Add node to graph or update existing node

         Returns: the node that was added or updated
        """

        if isinstance(node, str):
            node = Node(node, **kwargs)

        if not isinstance(node, Node):
            raise TypeError(f"node_id must be Node or str, not {type(node)}")

        if node.id in self.nodes:
            self.nodes[node.id].update(node)
        else:
            self.edges[node.id] = []
            self.nodes[node.id] = node

        return self.nodes[node.id]

    def add_edge(self, node_a: str | Node, node_b: str | Node, cost: Any):
        """ 
        Add edge to graph

        node_a and node_b must be node_ids or nodes

        """
        node_a = self.add_node(node_a)
        node_b = self.add_node(node_b)

        self.edges[node_a.id].append(Edge(node_a, node_b, cost))

    def add_nodes_from(self, nodes: list[Node | str]):
        """ Add nodes from a list of nodes """
        for node in nodes:
            self.add_node(node)

    def add_edges_from(self, edges: list[Edge | tuple | list]):
        """ Add edges from a list of edges"""
        for edge in edges:
            if isinstance(edge, Edge):
                self.add_edge(edge.source, edge.target, edge.cost)
            elif isinstance(edge, (tuple, list)):
                self.add_edge(edge[0], edge[1], edge[2])
            else:
                raise TypeError(f"Edge must be Edge, tuple or list, not {type(edge)}")
