""" soteriareitti/utils_graph.py """
from queue import PriorityQueue
import overpy

from soteriareitti.utils.utils_geo import GeoUtils, Location, Distance


class Node:
    """ Node class that represents a node in a graph """

    def __init__(self, identification: str, longitude: float, latitude: float):
        self.id = identification
        self.location = Location(longitude, latitude)

    def __repr__(self):
        return f"<utils_graph.Node id={self.id}, location={self.location}>"

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


class Edge:
    """ Edge class that represents an edge between two nodes """

    def __init__(self, source: Node, target: Node, distance: Distance = None):
        self.source = source
        self.target = target
        self.distance = distance if distance else GeoUtils.calculate_distance(
            source.location, target.location)

    def __repr__(self):
        return (f"<utils_graph.Edge source={self.source},"
                f"target={self.target}, distance={self.distance}>")


class Path:
    """ Path class that represents a path between multiple nodes """

    def __init__(self, nodes: list[Node] | None = None, distance: Distance | None = None):
        self.nodes = nodes if nodes else []
        if distance:
            self.distance = distance
        else:
            self.distance = Distance(0)
            for edge in list(zip(nodes[:-1], nodes[1:])):
                self.distance.add(GeoUtils.calculate_distance(
                    edge[0].location, edge[1].location))

    def __repr__(self):
        return f"<utils_graph.Path nodes={len(self.nodes)}, distance={self.distance}>"

    def __iter__(self):
        for node in self.nodes:
            yield node

    def __len__(self):
        return len(self.nodes)

    def add_node(self, node: Node, distance: Distance | None = None):
        """
        Add node to path 

        If distance is not given, it is calculated from the previous node
        """
        self.nodes.append(node)

        if distance:
            self.distance.add(distance)
        else:
            self.distance.add(GeoUtils.calculate_distance(
                self.nodes[-2].location, self.nodes[-1].location))

    def reverse(self):
        return Path(self.nodes[::-1], self.distance)


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

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

         If node is str, it is assumed to be an existing node's id

         Returns: the node that was added or updated
        """

        if isinstance(node, overpy.Node):
            node = Node.from_overpy_node(node)

        if isinstance(node, (tuple, list)):
            if len(node) != 3:
                raise ValueError(
                    f"Node must be a tuple or list of length 3, not {len(node)}")
            node = Node(*node)

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

    def add_edge(self, node_a: any, node_b: any, distance: Distance | None = None):
        """ 
        Add edge to graph

        node_a and node_b can be either a new node that is added/updated or an existing node's id

        """
        if not isinstance(distance, Distance) and distance is not None:
            raise TypeError(
                f"Distance must be Distance or None, not {type(distance)}")

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
    def _reconstruct_path(previous: dict[str], target: Node) -> Path:
        """ Reconstruct path from previous nodes """

        path = Path([target])

        while previous.get(target.id, False):
            edge = previous.get(target.id)
            target = edge.source
            path.add_node(target, edge.distance)

        return path.reverse()

    @staticmethod
    def dfs(graph: Graph, node: Node, visited: dict[str]) -> list[Node]:
        """ Depth-first search """
        if visited.get(node.id, False):
            return []

        visited[node.id] = True
        component = [node]

        for edge in graph.edges[node.id]:
            component += GraphUtils.dfs(graph, edge.target, visited)

        return component

    @staticmethod
    def get_largest_component(graph: Graph) -> Graph:
        """ Get largest component from graph """
        # TODO
        # Currently this exceeds pythons recursion limit with large graphs
        # This should be changed to iterative approach

        visited = {}
        largest_component = []

        for node in graph.get_nodes():
            new_component = GraphUtils.dfs(graph, node, visited)
            if len(new_component) > len(largest_component):
                largest_component = new_component

        # Create new graph from largest component
        new_graph = Graph()

        new_graph.add_nodes_from(largest_component)
        for edge in graph.get_edges():
            if edge.source.id in new_graph.nodes and edge.target.id in new_graph.nodes:
                new_graph.add_edge(edge.source, edge.target, edge.distance)

        return new_graph

    @staticmethod
    def dijkstra_shortest_path(graph: Graph, source: Node, target: Node) -> Path | None:
        """ 
        Dijkstra's algorithm
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm 
        """
        if source.id not in graph.nodes or target.id not in graph.nodes:
            return None

        queue = PriorityQueue()
        visited = {}
        distances = {}
        previous = {}

        distances[source.id] = Distance(0)
        queue.put((0, source))

        while not queue.empty():
            u_node = queue.get()[1]

            if u_node.id == target.id:
                return GraphUtils._reconstruct_path(previous, target)

            if visited.get(u_node.id, False):
                continue
            visited[u_node.id] = True

            for edge in graph.edges[u_node.id]:
                new_distance = distances.get(u_node.id, Distance(float("inf"))).add(edge.distance)
                old_distance = distances.get(edge.target.id, Distance(float("inf")))

                if new_distance.meters < old_distance.meters:
                    distances[edge.target.id] = new_distance
                    previous[edge.target.id] = edge
                    queue.put((new_distance.meters, edge.target))

        return None
