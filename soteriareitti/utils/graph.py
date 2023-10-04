""" soteriareitti/utils/graph.py """
from typing import Callable, Any
from queue import PriorityQueue


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

    @staticmethod
    def ida_star_shortest_path(graph: Graph, heuristic: Callable[[Node, Node], float],
                               source: Node, target: Node, delta: float = 0) -> Path | None:
        """
        Use IDA* algorithm to find shortest path from source to target 
        https://en.wikipedia.org/wiki/Iterative_deepening_A*

        args:
            - graph: Graph
            - heuristic: function that returns estimated cost from node to target as float
            - source: Node
            - target: Node
            - delta: float that determines an allowed error in the estimated cost. 
                The greater the delta, the faster the algorithm
        """

        def search(path: Path, limit: float) -> float:

            node = path.last
            estimated_cost = path.cost + heuristic(node, target)

            if node.id == target.id:
                return -1

            if estimated_cost > limit:
                return estimated_cost

            min_cost = float("inf")

            for edge in graph.edges[node.id]:
                if path.contains(edge.target):
                    continue

                path.add_node(edge.target, edge.cost)

                threshold = search(path, limit)
                if threshold < 0:
                    return threshold

                if threshold < min_cost:
                    min_cost = threshold

                path.pop()

            return min_cost

        limit = heuristic(source, target)
        path = Path.from_nodes([source])

        while True:
            threshold = search(path, limit)
            if threshold < 0:
                return path
            if threshold == float("inf"):
                return None
            limit = threshold + delta

    @staticmethod
    def dijkstra_shortest_path(graph: Graph, source: Node, target: Node) -> Path | None:
        """ Use Dijkstra's algorithm to find shortest path from source to target """
        previous = GraphUtils.dijkstras_algorithm(graph, source)
        path = GraphUtils.reconstruct_path(previous, source, target)
        if path:
            return path.reverse()
        return None

    @staticmethod
    def dijkstras_algorithm(graph: Graph, source: Node) -> dict[str, Edge]:
        """
        Dijkstra's algorithm
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm 

        returns: the `previous` dictionary

        The `previous` dictionary is used to keep track of the previous edge on the shortest path
        from the starting node to each node in the graph.
        It helps in reconstructing the shortest paths by specifying the sequence of edges to follow
        from the starting node to a specific destination node.

        Use reconstruct_path to reconstruct a Path from the `previous` dictionary 
        """
        if source.id not in graph.nodes:
            return None

        queue = PriorityQueue()
        visited = {}
        cost = {}
        previous = {}

        cost[source.id] = 0
        queue.put((0, source))

        while not queue.empty():
            u_node = queue.get()[1]

            if visited.get(u_node.id, False):
                continue
            visited[u_node.id] = True

            for edge in graph.edges[u_node.id]:
                new_distance = cost.get(u_node.id, float("inf")) + edge.cost
                old_distance = cost.get(edge.target.id, float("inf"))

                if new_distance < old_distance:
                    cost[edge.target.id] = new_distance
                    previous[edge.target.id] = edge
                    queue.put((new_distance, edge.target))

        return previous
