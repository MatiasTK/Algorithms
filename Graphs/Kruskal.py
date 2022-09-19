from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Inicializo el grafo con un diccionario.

    def add_edge(self, edge, value):
        self.graph[edge].append(value)

    def remove_edge(self, edge):
        del self.graph[edge]

    def __str__(self) -> str:
        return f"{dict(self.graph)}"

    def get_graph(self):
        return self.graph
