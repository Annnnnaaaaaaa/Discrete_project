class Graph:
    """
    Клас для представлення неорієнтованого зваженого графу для TSP.
    """

    def __init__(self, n, d):
        """
        Ініціалізація графу з n вершинами та щільністю d.

        Args:
            n (int): кількість вершин
            d (float): щільність графу
        """
        self.n = n
        self.density = d
        self.adj_matrix = [[0] * n for _ in range(n)]
        self.adj_list = {i: [] for i in range(n)}
        self.edge_count = 0

    def add_edge(self, u, v, weight):
        """Додає ребро між вершинами u та v з вагою weight."""
        if self.adj_matrix[u][v] == 0:
            self.edge_count += 1

        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

        self.adj_list[u] = [(neighbor, w) for neighbor, w in self.adj_list[u] if neighbor != v]
        self.adj_list[v] = [(neighbor, w) for neighbor, w in self.adj_list[v] if neighbor != u]

        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def get_edge_weight(self, u, v):
        """Повертає вагу ребра між u та v."""
        return self.adj_matrix[u][v]

    def has_edge(self, u, v):
        """Перевіряє, чи існує ребро між u та v."""
        return self.adj_matrix[u][v] > 0

    def get_neighbors(self, v):
        """Повертає список сусідів вершини v з вагами."""
        return self.adj_list[v]

    def degree(self, v):
        """Повертає ступінь вершини v."""
        return len(self.adj_list[v])

    def get_density(self):
        """Обчислює фактичну щільність графу."""
        max_edges = self.n * (self.n - 1) // 2
        return self.edge_count / max_edges if max_edges > 0 else 0

    def is_connected(self):
        """
        Перевіряє, чи є граф зв'язним за допомогою BFS.

        Returns:
            bool: True якщо граф зв'язний, False інакше
        """
        if self.n == 0:
            return True

        visited = [False] * self.n
        queue = [0]
        visited[0] = True
        count = 1

        while queue:
            v = queue.pop(0)
            for neighbor, _ in self.adj_list[v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1

        return count == self.n

    def __str__(self):
        """Текстове представлення графу."""
        return (f"Граф з {self.n} вершинами, {self.edge_count} ребрами, "
                f"щільність: {self.get_density():.2%}")