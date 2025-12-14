class GraphAdjList:
    """Граф на основі списків суміжності."""

    def __init__(self, n):
        self.n = n
        self.adj_list = {i: {} for i in range(n)}

    def add_edge(self, u, v, weight):
        self.adj_list[u][v] = weight
        self.adj_list[v][u] = weight

    def get_weight(self, u, v):
        return self.adj_list[u].get(v, float('inf'))

    def get_all_edges(self):
        """Повертає всі ребра графа у вигляді словника {(u, v): weight}."""
        edges = {}
        for u in range(self.n):
            for v, weight in self.adj_list[u].items():
                if u < v:  # Уникаємо дублікатів
                    edges[(u, v)] = weight
        return edges