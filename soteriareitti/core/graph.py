""" soteriareitti/core/graph.py """
import logging
import itertools
import networkx as nx
import overpy

from core._overpass import OverpassAPI
from utils.utils_graph import GraphUtils
from utils.utils_geo import GeoUtils, Location, Distance


class Graph:
    def __init__(self):
        self._overpass_api = OverpassAPI()

        # Tästä tulee myöhemmin oma tietorakenne
        self._graph = nx.DiGraph()

    def create_graph(self):
        logging.debug("Starting graph creation")
        data = self._overpass_api.get_place_data("Töölö")

        nodes = {}
        ways = {}

        for node in data.nodes:
            nodes[node.id] = {"lat": node.lat, "lon": node.lon}

        for way in data.ways:
            ways[way.id] = {"nodes": [group[0].id for group in itertools.groupby(way.nodes)]}

        self._graph.add_nodes_from(nodes.items())
        for way in ways.values():
            nodes = way.pop("nodes")
            edges = list(zip(nodes[:-1], nodes[1:]))
            self._graph.add_edges_from(edges)

        self._graph = GraphUtils.get_largest_component(self._graph)
        logging.debug("Graph creation done")

    def get_shortest_path(self, start, end) -> list | None:
        # Tämä toteutetaan myöhemmin omalla alogirtmillä
        logging.debug("Starting shortest path search")

        try:
            path = list(nx.shortest_path(self._graph, start, end))
        except nx.NetworkXNoPath:
            path = None

        return path

    def get_closest_node(self, location: Location) -> overpy.Node | None:
        """ Get closest node from a location that is atleast 50 meters close"""
        min_distance = Distance(50)

        data = self._overpass_api.get_around_data(location, min_distance)

        closest_node = None

        nodes: list[overpy.Node] = data.nodes
        for node in nodes:
            if not node.lon or not node.lat:
                continue

            distance_to_center = GeoUtils.calculate_distance(
                location, Location(float(node.lon), float(node.lat)))

            if distance_to_center.meters < min_distance.meters:
                closest_node = node
                min_distance = distance_to_center

        return closest_node

    @property
    def nodes(self) -> list:
        return list(self._graph.nodes(data=True))

    @property
    def edges(self) -> list:
        return list(self._graph.edges())
