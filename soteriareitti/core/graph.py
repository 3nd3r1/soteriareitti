""" soteriareitti/core/graph.py """
import logging
import itertools
import networkx as nx

from core._overpass import OverpassAPI
from utils.utils_graph import GraphUtils
from utils.utils_geo import GeoUtils, Location, Distance


class Graph:
    def __init__(self, user_interface):
        self._overpass_api = OverpassAPI()
        self._ui = user_interface

        # Tästä tulee myöhemmin oma tietorakenne
        self._graph = nx.DiGraph()

    def create_graph(self):
        logging.debug("Starting graph creation")
        data = self._overpass_api.get_overpass_place("Töölö")

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

    def get_closest_node(self, location: Location):
        bounding_box = GeoUtils.calculate_bbox(location, Distance(100))
        self._ui.create_marker(location)
        self._ui.create_marker(bounding_box.max_location)
        self._ui.create_marker(bounding_box.min_location)

        data = self._overpass_api.get_overpass_bbox(bounding_box)

        closest_node = None
        for node in data.nodes:
            logging.debug(node)

    @property
    def nodes(self) -> list:
        return list(self._graph.nodes(data=True))

    @property
    def edges(self) -> list:
        return list(self._graph.edges())
