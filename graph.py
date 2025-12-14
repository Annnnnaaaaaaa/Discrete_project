class Graph:
    """Повний неорієнтований зважений граф."""

    def __init__(self, n):
        self.n = n
        self.weights = {}

    def add_edge(self, u, v, weight):
        self.weights[(min(u, v), max(u, v))] = weight

    def get_weight(self, u, v):
        return self.weights[(min(u, v), max(u, v))]

    def get_all_edges(self):
        return self.weights