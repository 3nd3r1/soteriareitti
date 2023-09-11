import itertools

import networkx as nx

from core._overpass import OverpassAPI
from utils.utils_graph import GraphUtils
from utils.logger import logger


class Graph:
    def __init__(self):
        self.overpass_api = OverpassAPI()

        # Tästä tulee myöhemmin oma tietorakenne
        self._graph = nx.DiGraph()

    def create_graph(self):
        logger.debug("Starting graph creation")
        data = self.overpass_api.get_overpass_data("Töölö")

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
        logger.debug("Graph creation done")

    def get_shortest_path(self, start, end) -> list | None:
        # Tämä toteutetaan myöhemmin omalla alogirtmillä
        logger.debug("Starting shortest path search")

        try:
            path = list(nx.shortest_path(self._graph, start, end))
        except nx.NetworkXNoPath:
            path = None

        return path

    @property
    def nodes(self) -> list:
        return list(self._graph.nodes(data=True))

    @property
    def edges(self) -> list:
        return list(self._graph.edges())
