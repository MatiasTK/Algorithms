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

    def bfs(self, initial_vertex=0):
        visited = set()
        queue = []

        queue.append(initial_vertex)
        visited.add(initial_vertex)

        while queue:  # Mientras que haya elementos en la cola
            new_vertex = queue.pop(0)
            print(f"Se visitará el vertice {new_vertex}")

            for neighbour in self.graph[new_vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

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

g.bfs(2)

G = nx.Graph(dict(g.graph))
nx.draw_networkx(G)
plt.show()
