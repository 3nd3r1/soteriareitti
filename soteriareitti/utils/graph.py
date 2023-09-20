""" soteriareitti/utils/graph.py """
from queue import PriorityQueue
import overpy

from soteriareitti.utils.geo import GeoUtils, Location, Distance


class Node:
    """ Node class that represents a node in a graph """

    def __init__(self, identification: str, latitude: float, longitude: float):
        self.id = identification
        self.location = Location(latitude, longitude)

    def __repr__(self):
        return f"<soteriareitti.Node id={self.id}, location={self.location}>"

    @classmethod
    def from_overpy_node(cls, node: overpy.Node):
        if not isinstance(node, overpy.Node):
            raise TypeError(f"Node must be overpy.Node, not {type(node)}")
        if not node.lat or not node.lon:
            raise ValueError(f"Node {node.id} has no longitude or latitude")

        return cls(node.id, float(node.lat), float(node.lon))

    def update(self, node: "Node"):
        """ Update node with data from another node """
        if not isinstance(node, Node):
            raise TypeError(f"Node must be Node, not {type(node)}")

        self.location = node.location


class Edge:
    """ Edge class that represents an edge between two nodes """

    def __init__(self, source: Node, target: Node, distance: Distance | None = None):
        self.source = source
        self.target = target
        self.distance = distance if distance else GeoUtils.calculate_distance(
            source.location, target.location)

    def __repr__(self):
        return (f"<soteriareitti.Edge source={self.source},"
                f"target={self.target}, distance={self.distance}>")


class Path:
    """ Path class that represents a path between multiple nodes """

    def __init__(self, edges: list[Edge] | None = None):
        self.distance = Distance(0)
        self.__visited = {}

        if edges:
            for edge in edges:
                if not isinstance(edge, Edge):
                    raise TypeError(f"Edge must be Edge, not {type(edge)}")
                self.distance += edge.distance
                self.__visited[edge.target.id] = True
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
        return f"<soteriareitti.Path nodes={len(self)}, distance={self.distance}>"

    def __iter__(self):
        for edge in self.__edges:
            yield edge.target

    def __len__(self):
        return len(self.__edges)

    def add_node(self, node: Node, distance: Distance | None = None):
        """
        Add node to path 

        If distance is not given, it is calculated from the previous node
        """
        self.__visited[node.id] = True
        if self.last:
            new_edge = Edge(self.last, node, distance)
            self.__edges.append(new_edge)
            self.distance += new_edge.distance
        else:
            self.__edges.append(Edge(node, node, Distance(0)))

    def pop(self) -> Node:
        self.distance -= self.__edges[-1].distance
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
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def __repr__(self) -> str:
        return f"<soteriareitti.Graph nodes={len(self.nodes)}, edges={len(self.get_edges())}>"

    def get_nodes(self) -> list[Node]:
        """ Get all nodes """
        return list(self.nodes.values())

    def get_edges(self) -> list[Edge]:
        """ Get all edges """
        edges = []
        for edge_list in self.edges.values():
            edges += edge_list
        return edges

    def add_node(self, node: overpy.Node | Node | str | tuple | list):
        """
         Add node to graph or update existing node

         - If node is str, it is assumed to be an existing node's id
         - If node is tuple or list, it is assumed to be a new node 
         of format (id, latitude, longitude)

         Returns: the node that was added or updated
        """

        if isinstance(node, overpy.Node):
            node = Node.from_overpy_node(node)

        if isinstance(node, (tuple, list)):
            if len(node) != 3:
                raise ValueError(
                    f"Node must be a tuple or list of length 3, not {len(node)}")
            node = Node(str(node[0]), float(node[1]), float(node[2]))

        if isinstance(node, str):
            if node not in self.nodes:
                raise ValueError(f"Node {node} does not exist")
            return self.nodes[node]

        if not isinstance(node, Node):
            raise TypeError(
                f"Node must be overpy.Node, graph_utils.Node"
                f"or a node's id (str), not {type(node)}")

        if node.id not in self.nodes:
            self.edges[node.id] = []
            self.nodes[node.id] = node
        else:
            self.nodes[node.id].update(node)

        return self.nodes[node.id]

    def add_edge(self, node_a: any, node_b: any, distance: Distance | float | int | None = None):
        """ 
        Add edge to graph

        node_a and node_b can be either a new node that is added/updated or an existing node's id
        distance is optional and can be either a Distance object or a float

        """
        if isinstance(distance, (float, int)):
            distance = Distance(float(distance))

        if not isinstance(distance, Distance) and distance is not None:
            raise TypeError(
                f"Distance must be Distance, float or None, not {type(distance)}")

        node_a = self.add_node(node_a)
        node_b = self.add_node(node_b)

        self.edges[node_a.id].append(Edge(node_a, node_b, distance))

    def add_nodes_from(self, nodes: list[any]):
        """ Add nodes from a list of nodes """
        for node in nodes:
            self.add_node(node)

    def add_edges_from(self, edges: list[any]):
        """ Add edges from a list of edges"""
        for edge in edges:
            if isinstance(edge, Edge):
                self.add_edge(edge.source, edge.target, edge.distance)
            elif isinstance(edge, (tuple, list)):
                self.add_edge(edge[0], edge[1], edge[2] if len(edge) > 2 else None)
            else:
                raise TypeError(f"Edge must be Edge, tuple or list, not {type(edge)}")


class GraphUtils:
    @staticmethod
    def reconstruct_path(previous: dict, source: Node, target: Node) -> Path | None:
        """ Reconstruct path from `previous` dictionary """

        current_edge = previous.get(target.id)
        path = Path.from_nodes([target])

        while current_edge:
            path.add_node(current_edge.source, current_edge.distance)
            if current_edge.source.id == source.id:
                return path
            current_edge = previous.get(current_edge.source.id)

        return None

    @staticmethod
    def reverse_graph(graph: Graph) -> Graph:
        """ Reverse all edges in a directional graph """
        edges = graph.get_edges()
        reversed_edges = [Edge(edge.target, edge.source, edge.distance) for edge in edges]

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

                if current_node.id in component or visited.get(current_node.id, False):
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
                new_graph.add_edge(edge.source, edge.target, edge.distance)

        return new_graph

    @staticmethod
    def ida_star_shortest_path(graph: Graph, source: Node, target: Node) -> Path | None:
        """
        Use IDA* algorithm to find shortest path from source to target 
        https://en.wikipedia.org/wiki/Iterative_deepening_A*
        """

        def heuristic(node: Node) -> Distance:
            return GeoUtils.calculate_distance(node.location, target.location)

        def search(path: Path, limit: Distance) -> Distance:

            node = path.last
            estimated_cost = path.distance + heuristic(node)

            if node.id == target.id:
                return Distance(-1)

            if estimated_cost > limit:
                return estimated_cost

            min_distance = Distance(float("inf"))

            for edge in graph.edges[node.id]:
                if path.contains(edge.target):
                    continue

                path.add_node(edge.target, edge.distance)

                threshold = search(path, limit)
                if threshold < 0:
                    return threshold

                if threshold < min_distance:
                    min_distance = threshold

                path.pop()

            return min_distance

        limit = heuristic(source)
        path = Path.from_nodes([source])

        while True:
            threshold = search(path, limit)
            if threshold < 0:
                return path
            if threshold == float("inf"):
                return None
            # One meter is added to the threshold for faster convergence
            # A meters inaccuracy is acceptable
            limit = threshold + 1

    @staticmethod
    def dijkstra_shortest_path(graph: Graph, source: Node, target: Node) -> Path | None:
        """ Use Dijkstra's algorithm to find shortest path from source to target """
        previous = GraphUtils.dijkstras_algorithm(graph, source)
        print(previous)
        return GraphUtils.reconstruct_path(previous, source, target).reverse()

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
        distances = {}
        previous = {}

        distances[source.id] = Distance(0)
        queue.put((0, source))

        while not queue.empty():
            u_node = queue.get()[1]

            if visited.get(u_node.id, False):
                continue
            visited[u_node.id] = True

            for edge in graph.edges[u_node.id]:
                new_distance = distances.get(u_node.id, Distance(float("inf"))) + edge.distance
                old_distance = distances.get(edge.target.id, Distance(float("inf")))

                if new_distance.meters < old_distance.meters:
                    distances[edge.target.id] = new_distance
                    previous[edge.target.id] = edge
                    queue.put((new_distance.meters, edge.target))

        return previous
