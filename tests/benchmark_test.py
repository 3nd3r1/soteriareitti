# pylint: disable-all

import random
import time

from soteriareitti.core.map import Map
from soteriareitti.utils.graph import GraphUtils


def random_node(graph):
    return random.choice(graph.get_nodes())


def run_test(map: Map, place: str):
    map.load_place(place)
    graph = map._graph

    source = random_node(graph)
    target = random_node(graph)

    time_before = time.time()
    path_ida = map.get_shortest_path(source.location, target.location)
    time_ida = time.time()-time_before

    time_before = time.time()
    path_dijkstra = GraphUtils.dijkstra_shortest_path(graph, source, target)
    time_dijkstra = time.time()-time_before

    print(f"Benchmarks were ran on graph: {graph}")
    print(f"IDA* algorithm took {time_ida} s to find path: {path_ida}")
    print(f"Dijkstras algorithm took {time_dijkstra} s to find path: {path_dijkstra}")
    print()


if __name__ == "__main__":
    map = Map()

    # Tests in Paloheinä (small)
    run_test(map, "Paloheinä")

    # Tests in Töölö (small)
    run_test(map, "Töölö")

    # Tests in Helsinki (large)
    run_test(map, "Helsinki")
