# pylint: disable-all

import random
import time

from soteriareitti.utils.geo import GeoUtils, Location
from soteriareitti.utils.graph import GraphUtils, Graph


def generate_random_coordinates():
    latitude = random.uniform(48.0, 52.0)
    longitude = random.uniform(2.0, 6.0)
    return Location(latitude, longitude)


def generate_graph(nodes_count, edges_per_node_min, edges_per_node_max):
    graph = Graph()

    for node in range(1, nodes_count+1):
        graph.add_node(str(node), location=generate_random_coordinates())

    for node in graph.get_nodes():
        for _ in range(random.randint(edges_per_node_min, edges_per_node_max)):
            node_t = random.choice(graph.get_nodes())
            graph.add_edge(node, node_t, GeoUtils.calculate_distance(
                node.location, node_t.location).meters)
    return graph


def random_node(graph):
    return random.choice(graph.get_nodes())


def heuristic(node, target):
    return GeoUtils.calculate_distance(node.location, target.location).meters


if __name__ == "__main__":
    i = 1
    while i <= 1000:
        nodes_count = 5 * i
        edges_per_node_min = 3
        edges_per_node_max = 8
        graph = generate_graph(nodes_count, edges_per_node_min, edges_per_node_max)
        source = random_node(graph)
        target = random_node(graph)

        time_before = time.time()
        path_ida = GraphUtils.ida_star_shortest_path(graph, heuristic, source, target)
        time_ida = time.time()-time_before

        time_before = time.time()
        path_dijk = GraphUtils.dijkstra_shortest_path(graph, source, target)
        time_dijkstra = time.time()-time_before

        print(f"Benchmarks were ran on graph: {graph}")
        print(f"IDA* algorithm took {time_ida} s to find path: {path_ida}")
        print(f"Dijkstras algorithm took {time_dijkstra} s to find path: {path_dijk}")
        print()
        i *= 10
