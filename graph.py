class Graph:
    """
    Клас для представлення неорієнтованого зваженого графу для TSP.
    Всі графи є зваженими з щільністю від середньої до високої.
    Підтримує обидва представлення: матрицю суміжності та списки суміжності.
    """

    def __init__(self, n):
        """
        Ініціалізація графу з n вершинами.

        Args:
            n (int): кількість вершин
        """
        self.n = n
        # Матриця ваг (0 означає відсутність ребра)
        self.adj_matrix = [[0] * n for _ in range(n)]
        # Списки суміжності: {вершина: [(сусід, вага), ...]}
        self.adj_list = {i: [] for i in range(n)}
        # Кількість ребер
        self.edge_count = 0

    def add_edge(self, u, v, weight):
        """
        Додає ребро між вершинами u та v з вагою weight.

        Args:
            u (int): перша вершина (0 <= u < n)
            v (int): друга вершина (0 <= v < n)
            weight (float): вага ребра (> 0)
        """
        # Якщо ребро вже існує, не рахуємо його повторно
        if self.adj_matrix[u][v] == 0:
            self.edge_count += 1

        # Додаємо в матрицю ваг (симетрично для неорієнтованого графу)
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

        # Оновлюємо списки суміжності
        self.adj_list[u] = [(neighbor, w) for neighbor, w in self.adj_list[u] if neighbor != v]
        self.adj_list[v] = [(neighbor, w) for neighbor, w in self.adj_list[v] if neighbor != u]

        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def get_edge_weight(self, u, v):
        """
        Повертає вагу ребра між u та v.

        Args:
            u (int): перша вершина
            v (int): друга вершина

        Returns:
            float: вага ребра або 0, якщо ребра немає
        """
        return self.adj_matrix[u][v]

    def has_edge(self, u, v):
        """
        Перевіряє, чи існує ребро між u та v.

        Args:
            u (int): перша вершина
            v (int): друга вершина

        Returns:
            bool: True якщо ребро існує
        """
        return self.adj_matrix[u][v] > 0

    def get_neighbors(self, v):
        """
        Повертає список сусідів вершини v.

        Args:
            v (int): вершина

        Returns:
            list: список кортежів (сусід, вага)
        """
        return self.adj_list[v]

    def get_all_neighbors(self, v):
        """
        Повертає всіх сусідів вершини v (тільки індекси).

        Args:
            v (int): вершина

        Returns:
            list: список індексів сусідів
        """
        return [neighbor for neighbor, _ in self.adj_list[v]]

    def degree(self, v):
        """
        Повертає ступінь вершини v.

        Args:
            v (int): вершина

        Returns:
            int: ступінь вершини
        """
        return len(self.adj_list[v])

    def get_density(self):
        """
        Обчислює щільність графу.

        Returns:
            float: щільність (відношення кількості ребер до максимальної)
        """
        max_edges = self.n * (self.n - 1) // 2
        return self.edge_count / max_edges if max_edges > 0 else 0

    def is_connected(self):
        """
        Перевіряє, чи є граф зв'язним (за допомогою BFS).

        Returns:
            bool: True якщо граф зв'язний
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

    def get_all_edges(self):
        """
        Повертає список всіх ребер графу.

        Returns:
            list: список кортежів (u, v, weight)
        """
        edges = []
        for u in range(self.n):
            for v, weight in self.adj_list[u]:
                if u < v:  # щоб не додавати ребро двічі
                    edges.append((u, v, weight))
        return edges

    def __str__(self):
        """
        Текстове представлення графу.
        """
        return (f"Граф з {self.n} вершинами, {self.edge_count} ребрами, "
                f"щільність: {self.get_density():.2%}")

    def print_adj_matrix(self):
        """
        Виводить матрицю суміжності.
        """
        print("Матриця суміжності:")
        for row in self.adj_matrix:
            print([f"{x:6.1f}" for x in row])

    def print_adj_list(self):
        """
        Виводить списки суміжності.
        """
        print("Списки суміжності:")
        for v in range(self.n):
            neighbors = ', '.join([f"{u}(w={w:.1f})" for u, w in self.adj_list[v]])
            print(f"{v}: [{neighbors}]")