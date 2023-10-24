""" soteriareitti/algorithms/dijkstra.py """
import logging
from queue import PriorityQueue

from soteriareitti.classes.graph import Graph, Node, Edge, Path
from soteriareitti.utils.graph import GraphUtils


class Dijkstra:
    @staticmethod
    def get_shortest_path(graph: Graph, source: Node, target: Node) -> Path | None:
        """ Use Dijkstra's algorithm to find shortest path from source to target """
        logging.debug("Dijkstra's shortest path search started")
        previous = Dijkstra.get_data(graph, source, target)
        path = GraphUtils.reconstruct_path(previous, source, target)
        if path:
            return path.reverse()
        return None

    @staticmethod
    def get_data(graph: Graph, source: Node, target: Node | None = None) -> dict[str, Edge]:
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

            if target and u_node.id == target.id:
                break

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
