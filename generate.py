import random


class GraphGenerator:
    """Генератор простих неорієнтованих зважених графів."""

    @staticmethod
    def generate(graph, min_weight=1, max_weight=100):
        """
        Наповнює граф ребрами відповідно до його щільності.

        Args:
            graph (Graph): об'єкт графу з вже встановленими n та density
            min_weight (float): мінімальна вага ребра
            max_weight (float): максимальна вага ребра

        Returns:
            Graph: той самий граф, але з доданими ребрами
        """
        n = graph.n
        density = graph.density

        max_edges = n * (n - 1) // 2
        target_edges = int(max_edges * density)

        all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
        random.shuffle(all_edges)
        selected_edges = all_edges[:target_edges]

        for u, v in selected_edges:
            weight = random.uniform(min_weight, max_weight)
            graph.add_edge(u, v, weight)

        return graph