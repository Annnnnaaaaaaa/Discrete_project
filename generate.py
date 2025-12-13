import random


class GraphGenerator:
    """Генератор простих неорієнтованих зважених гамільтонових графів."""

    @staticmethod
    def generate(graph, min_weight=1, max_weight=100):
        """
        Наповнює граф ребрами відповідно до його щільності.
        Гарантує, що граф буде гамільтоновим.

        Args:
            graph (Graph): об'єкт графу з вже встановленими n та density
            min_weight (float): мінімальна вага ребра
            max_weight (float): максимальна вага ребра

        Returns:
            Graph: гамільтонів граф з доданими ребрами
        """
        n = graph.n
        density = graph.density
        max_edges = n * (n - 1) // 2
        target_edges = int(max_edges * density)

        # Генеруємо доки не отримаємо гамільтонів граф
        while True:
            # Очищуємо граф перед новою спробою
            GraphGenerator._clear_graph(graph)

            # Генеруємо ребра
            all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
            random.shuffle(all_edges)
            selected_edges = all_edges[:target_edges]

            for u, v in selected_edges:
                weight = random.uniform(min_weight, max_weight)
                graph.add_edge(u, v, weight)

            # Перевіряємо на гамільтоновість
            if GraphGenerator._is_hamiltonian(graph):
                return graph

    @staticmethod
    def _is_hamiltonian(graph):
        """
        Перевіряє граф на гамільтоновість за теоремою Дірака.
        Теорема Дірака: якщо для кожної вершини v графу deg(v) >= n/2,
        то граф має гамільтонів цикл.

        Args:
            graph (Graph): граф для перевірки

        Returns:
            bool: True, якщо граф задовольняє умову Дірака
        """
        n = graph.n

        # Граф повинен бути зв'язним
        if not graph.is_connected():
            return False

        # Перевірка умови Дірака: deg(v) >= n/2 для всіх вершин
        for v in range(n):
            if graph.degree(v) < n / 2:
                return False

        return True

    @staticmethod
    def _clear_graph(graph):
        """
        Очищує граф (видаляє всі ребра).

        Args:
            graph (Graph): граф для очищення
        """
        n = graph.n
        graph.adj_matrix = [[0] * n for _ in range(n)]
        graph.adj_list = {i: [] for i in range(n)}
        graph.edge_count = 0