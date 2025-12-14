class GraphAdjMatrix:
    """Граф на основі матриці суміжності."""

    def __init__(self, n):
        self.n = n
        self.matrix = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            self.matrix[i][i] = 0

    def add_edge(self, u, v, weight):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight

    def get_weight(self, u, v):
        return self.matrix[u][v]

    def get_all_edges(self):
        """Повертає всі ребра графа у вигляді словника {(u, v): weight}."""
        edges = {}
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.matrix[i][j] != float('inf'):
                    edges[(i, j)] = self.matrix[i][j]
        return edges