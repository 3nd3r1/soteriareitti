""" soteriareitti/algorithms/ida_star.py """
import logging
from typing import Callable
from soteriareitti.classes.graph import Graph, Node, Edge, Path


class IdaStar:
    min_cost = {}

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

        logging.debug("IDA* shortest path search started")
        limit = heuristic(source, target)
        IdaStar.min_cost.clear()
        path = Path.from_nodes([source])

        while True:
            threshold = IdaStar.search(graph, heuristic, path, target, limit, delta/10000)
            if threshold < 0:
                logging.debug("Found IDA* shortest path: %s", path)
                return path
            if threshold == float("inf"):
                return None
            limit = threshold + delta

    @staticmethod
    def search(graph: Graph, heuristic: Callable[[Node, Node], float],
               path: Path, target: Node, limit: float, delta: float) -> float:
        """ IDA* search method. Uses iterative depth-first search """

        stack = [(Edge(path.last, path.last, 0), 0)]
        min_threshold = float("inf")
        path.pop()

        while stack:
            edge, depth = stack.pop()
            path.add_node(edge.target, edge.cost)
            node = path.last

            f_value = path.cost + heuristic(node, target)
            if f_value > limit:
                min_threshold = min(min_threshold, f_value)
                for _ in range(depth):
                    path.pop()
                continue

            if node == target:
                return -1

            if path.cost-delta > IdaStar.min_cost.get(node.id, float("inf")):
                for _ in range(depth):
                    path.pop()
                continue

            IdaStar.min_cost[node.id] = path.cost

            if len(graph.edges[node.id]) == 0:
                for _ in range(depth):
                    path.pop()
                continue

            successors = sorted(graph.edges[node.id], key=lambda e: -heuristic(e.target, target))
            for index, edge in enumerate(successors):
                next_depth = depth + 1 if index == 0 else 1
                stack.append((edge, next_depth))

        return min_threshold
