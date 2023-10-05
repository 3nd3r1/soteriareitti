""" soteriareitti/algorithms/ida_star.py """
from typing import Callable
from soteriareitti.classes.graph import Graph, Node, Path


class IdaStar:
    @staticmethod
    def get_shortest_path(graph: Graph, heuristic: Callable[[Node, Node], float],
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

        limit = heuristic(source, target)
        path = Path.from_nodes([source])

        while True:
            threshold = IdaStar.search(graph, heuristic, target, path, limit)
            if threshold < 0:
                return path
            if threshold == float("inf"):
                return None
            limit = threshold + delta

    @staticmethod
    def search(graph: Graph, heuristic: Callable[[Node, Node], float],
               target: Node, path: Path, limit: float) -> float:

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

            threshold = IdaStar.search(graph, heuristic, target, path, limit)
            if threshold < 0:
                return threshold

            if threshold < min_cost:
                min_cost = threshold

            path.pop()

        return min_cost
