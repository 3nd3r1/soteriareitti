""" soteriareitti/algorithms/ida_star.py """
import logging
from typing import Callable
from soteriareitti.classes.graph import Graph, Node, Edge, Path
from soteriareitti.utils.graph import GraphUtils


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

        logging.debug("IDA* shortest path search started")
        limit = heuristic(source, target)
        previous = {}

        while True:
            threshold = IdaStar.search(graph, heuristic, previous, source, target, limit)
            if threshold < 0:
                path = GraphUtils.reconstruct_path(previous, source, target).reverse()
                logging.debug("Found IDA* shortest path: %s", path)
                return path
            if threshold == float("inf"):
                return None
            limit = threshold + delta

    @staticmethod
    def search(graph: Graph, heuristic: Callable[[Node, Node], float],
               previous: dict[str, Edge], source: Node, target: Node, limit: float) -> float:
        """ IDA* search method. Uses iterative depth-first search """
        min_cost = float("inf")
        stack = [source]
        previous.clear()
        cost = {}
        cost[source.id] = 0

        while stack:
            node = stack.pop()
            threshold = cost[node.id] + heuristic(node, target)

            if node.id == target.id:
                return -1
            if threshold > limit:
                min_cost = min(min_cost, threshold)
                continue

            for edge in graph.edges[node.id]:
                if cost[node.id]+edge.cost < cost.get(edge.target.id, float("inf")):
                    previous[edge.target.id] = edge
                    cost[edge.target.id] = cost[node.id]+edge.cost
                    stack.append(edge.target)

        return min_cost
