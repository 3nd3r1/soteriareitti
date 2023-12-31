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


def heuristic(node, target_node) -> float:
    """ Minutes to travel from node to target node """
    return GeoUtils.calculate_time(node.location,
                                   target_node.location, average_speed).minutes


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

    print(f"Benchmarks were ran in {place} ({graph})")
    print(f"AVG speed: {average_speed}")
    print(f"IDA* algorithm took {time_ida} s to find path: {path_ida}")
    print(f"Dijkstra's algorithm took {time_dijkstra} s to find path: {path_dijkstra}")
    print("")


if __name__ == "__main__":
    configure_logging(True)
    map = Map()

    # Tests in Sipoo (small)
    run_test(map, "Sipoo")

    # Tests in Kirkkonummi (medium)
    run_test(map, "Kirkkonummi")

    # Tests in Espoo (semi-large)
    run_test(map, "Espoo")

    # Tests in Helsinki (large)
    run_test(map, "Helsinki")
