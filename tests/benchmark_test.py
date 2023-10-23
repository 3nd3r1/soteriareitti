# pylint: disable-all
import random
import time

from soteriareitti.core.map import Map

from soteriareitti.algorithms.dijkstra import Dijkstra
from soteriareitti.algorithms.ida_star import IdaStar

from soteriareitti.utils.geo import GeoUtils

from soteriareitti.utils.logging import configure_logging


def random_node(graph):
    return random.choice(graph.get_nodes())


average_speed = None


dp = {}


def heuristic(node, target_node) -> float:
    """ Minutes to travel from node to target node """
    if dp.get(node.id, False):
        return dp.get(node.id)

    dp[node.id] = GeoUtils.calculate_time(node.location,
                                          target_node.location, average_speed).minutes
    return dp[node.id]


def run_test(map: Map, place: str):
    global average_speed
    global dp
    map.load_place(place)
    dp = {}
    graph = map._graph
    average_speed = map._average_speed

    source = random_node(graph)
    target = random_node(graph)

    time_before = time.time()
    path_ida = IdaStar.get_shortest_path(graph, heuristic, source, target, delta=0.1)
    time_ida = time.time()-time_before

    time_before = time.time()
    path_dijkstra = Dijkstra.get_shortest_path(graph, source, target)
    time_dijkstra = time.time()-time_before

    print(f"Benchmarks were ran on graph: {graph}")
    print(f"AVG speed: {average_speed}")
    print(f"IDA* algorithm took {time_ida} s to find path: {path_ida}")
    print(f"Dijkstras algorithm took {time_dijkstra} s to find path: {path_dijkstra}")
    print("")


if __name__ == "__main__":
    configure_logging(True)
    map = Map()

    # Tests in Paloheinä (small)
    run_test(map, "Paloheinä")

    # Tests in Töölö (small)
    run_test(map, "Töölö")

    # Tests in Helsinki (large)
    run_test(map, "Helsinki")
