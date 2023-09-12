""" soteriareitti/utils_graph.py """
import networkx as nx


class GraphUtils:
    @staticmethod
    def get_largest_component(graph):
        """
        Get subgraph of graph's largest weakly connected component.

        From: https://github.com/gboeing/osmnx/blob/main/osmnx/utils_graph.py#L282
        """
        is_connected = nx.is_weakly_connected
        connected_components = nx.weakly_connected_components

        if not is_connected(graph):
            # get all the connected components in graph then identify the largest
            largest_cc = max(connected_components(graph), key=len)

            # induce (frozen) subgraph then unfreeze it by making new MultiDiGraph
            graph = nx.MultiDiGraph(graph.subgraph(largest_cc))

        graph.remove_nodes_from(list(nx.isolates(graph)))
        return graph
