from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt  # Necesario para dibujar networkX


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Inicializo el grafo con un diccionario.

    def add_edge(self, edge, value):
        self.graph[edge].append(value)

    def remove_edge(self, edge):
        del self.graph[edge]

    def visit_nodes_dfs(self, vertex, visited):
        visited.add(vertex)
        print(f"Se visito al vertice {vertex} y se lo agrego a visitados")

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.visit_nodes_dfs(neighbour, visited)

    def dfs(self, initial_vertex=0):
        visited = set()  # No va a haber duplicados en los visitados

        self.visit_nodes_dfs(initial_vertex, visited)

        print(f"Los vertices visitados fueron: {visited}")

    def __str__(self) -> str:
        return f"{dict(self.graph)}"

    def get_graph(self):
        return self.graph


g = Graph()
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 6)
g.add_edge(6, 2)
g.add_edge(6, 4)
g.add_edge(4, 6)
g.add_edge(1, 3)
g.add_edge(3, 1)
g.add_edge(3, 7)
g.add_edge(7, 3)

G = nx.Graph(dict(g.graph))
nx.draw_networkx(G)
plt.show()

g.dfs(2)
