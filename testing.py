from networkx import DiGraph
from vrpy import VehicleRoutingProblem

G = DiGraph()

G.add_edge("Source", 1, cost=1)
G.add_edge("Source", 2, cost=2)
G.add_edge("Source", 3, cost=3)
G.add_edge(1, "Sink", cost=1)
G.add_edge(2, "Sink", cost=2)
G.add_edge(3, "Sink", cost=3)
G.add_edge(1, 2, cost=3)
G.add_edge(2, 1, cost=3)
G.add_edge(1, 3, cost=4)
G.add_edge(3, 1, cost=4)
G.add_edge(2, 3, cost=2)
G.add_edge(3, 2, cost=2)

G.nodes[1]["demand"] = 9
G.nodes[2]["demand"] = 7
G.nodes[3]["demand"] = 2

prob = VehicleRoutingProblem(G, load_capacity=10)
prob.solve(heuristic_only=True)

print(prob.best_routes)
