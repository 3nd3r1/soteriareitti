# pylint: disable-all

import random
import time
import cProfile

from soteriareitti.core.map import Map

from soteriareitti.algorithms.dijkstra import Dijkstra
from soteriareitti.algorithms.ida_star import IdaStar

from soteriareitti.classes.geo import Speed
from soteriareitti.utils.geo import GeoUtils


def random_node(graph):
    return random.choice(graph.get_nodes())


def heuristic(node, target_node) -> float:
    """ Minutes to travel from node to target node """
    average_speed = Speed((node.maxspeed.kilometers_hour +
                           target_node.maxspeed.kilometers_hour)/2)
    return GeoUtils.calculate_time(node.location,
                                   target_node.location, average_speed).minutes


def run_test(map: Map, place: str):
    map.load_place(place)
    graph = map._graph

    source = random_node(graph)
    target = random_node(graph)

    time_before = time.time()
    path_ida = IdaStar.get_shortest_path(graph, heuristic, source, target, delta=0.1)
    time_ida = time.time()-time_before

    time_before = time.time()
    path_dijkstra = Dijkstra.get_shortest_path(graph, source, target)
    time_dijkstra = time.time()-time_before

    print("Benchmarks were ran on graph: %s", graph)
    print("IDA* algorithm took %s s to find path: %s", time_ida, path_ida)
    print("Dijkstras algorithm took %s s to find path: %s", time_dijkstra, path_dijkstra)
    print("")


if __name__ == "__main__":
    map = Map()

    # Tests in Paloheinä (small)
    run_test(map, "Paloheinä")

    # Tests in Töölö (small)
    run_test(map, "Töölö")

    # Tests in Helsinki (large)
    run_test(map, "Helsinki")
