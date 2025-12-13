import random
from graph import Graph


class GraphGenerator:
    """Генератор простих неорієнтованих зважених графів."""

    @staticmethod
    def generate(n, density, min_weight=1, max_weight=100):
        """
        Генерує простий неорієнтований зважений граф заданої щільності.

        Args:
            n (int): кількість вершин
            density (float): щільність графу (0 < density <= 1)
            min_weight (float): мінімальна вага ребра
            max_weight (float): максимальна вага ребра

        Returns:
            Graph: згенерований граф
        """
        graph = Graph(n, density)  # ← ВИПРАВЛЕНО: передаємо density

        max_edges = n * (n - 1) // 2
        target_edges = int(max_edges * density)

        all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
        random.shuffle(all_edges)
        selected_edges = all_edges[:target_edges]

        for u, v in selected_edges:
            weight = random.uniform(min_weight, max_weight)
            graph.add_edge(u, v, weight)

        return graph