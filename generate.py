import random


class GraphGenerator:
    """
    Генератор простих неорієнтованих зважених графів.
    """

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
        graph = Graph(n)

        # Максимальна кількість ребер у простому неорієнтованому графі
        max_edges = n * (n - 1) // 2

        # Необхідна кількість ребер для заданої щільності
        target_edges = int(max_edges * density)

        # Створюємо список всіх можливих ребер
        all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]

        # Перемішуємо і беремо потрібну кількість
        random.shuffle(all_edges)
        selected_edges = all_edges[:target_edges]

        # Додаємо вибрані ребра з випадковими вагами
        for u, v in selected_edges:
            weight = random.uniform(min_weight, max_weight)
            graph.add_edge(u, v, weight)

        return graph