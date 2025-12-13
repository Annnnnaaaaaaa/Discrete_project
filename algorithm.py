from graph import Graph
from generate import GraphGenerator
import sys

# Використовуємо велике число для представлення "нескінченності" (відсутність прямого ребра)
INF = sys.maxsize


class Algorithm:
    def __init__(self, g: Graph):
        self.g = g
        # Ця матриця буде зберігати найкоротші шляхи між усіма вершинами
        self.full_distances_matrix = self._floyd_warshall()

    def _floyd_warshall(self):
        """
        Реалізація алгоритму Флойда-Уоршелла для знаходження найкоротших шляхів між усіма парами вершин.
        """
        V = self.g.n
        # Ініціалізуємо матрицю відстаней на основі матриці суміжності графа
        # Перетворюємо 0 на INF, якщо немає ребра (для неповного графа)
        dist = [[0] * V for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if i == j:
                    dist[i][j] = 0
                elif self.g.has_edge(i, j):
                    dist[i][j] = self.g.get_edge_weight(i, j)
                else:
                    dist[i][j] = INF

        # Основні цикли алгоритму
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    def find_tsp_nearest_neighbor(self, start_city=0):
        """
        Евристика найближчого сусіда для TSP, використовуючи матрицю повних відстаней.
        """
        n = self.g.n
        visited = [False] * n
        route = []
        current_city = start_city
        route.append(current_city)
        visited[current_city] = True
        total_distance = 0

        for _ in range(1, n):
            nearest_city = -1
            min_dist = INF

            for city in range(n):
                if not visited[city] and self.full_distances_matrix[current_city][city] < min_dist:
                    min_dist = self.full_distances_matrix[current_city][city]
                    nearest_city = city

            if nearest_city != -1:
                route.append(nearest_city)
                visited[nearest_city] = True
                total_distance += min_dist
                current_city = nearest_city
            else:
                print("Помилка: Граф не є сильно зв'язним, маршрут неможливо завершити.")
                return None, INF

        # Повертаємося до початкового міста, щоб замкнути цикл TSP
        total_distance += self.full_distances_matrix[route[-1]][start_city]
        route.append(start_city)

        return route, total_distance

    def execute_tsp(self):
        """
        Основна функція для виконання TSP після обчислення всіх шляхів.
        """

        # Перевіряємо зв'язність графа перед запуском TSP
        for i in range(self.g.n):
            for j in range(self.g.n):
                if self.full_distances_matrix[i][j] == INF:
                    print(f"Граф не є повністю зв'язним (немає шляху між {i} та {j}).")
                    print("Неможливо виконати TSP, що охоплює всі вершини.")
                    return

        print("\nГраф є зв'язним. Запускаємо TSP методом найближчого сусіда...")
        route, distance = self.find_tsp_nearest_neighbor(start_city=0)

        if route:
            print(f"\nЗнайдений маршрут TSP: {' -> '.join(map(str, route))}")
            print(f"Загальна довжина маршруту: {distance:.2f}")


# --- Приклад використання (додано для демонстрації) ---
# if __name__ == "__main__":
    # Створюємо об'єкт графу з параметрами
    # Щільність 0.5 (50%) робить його неповним
    graph = Graph(n=10, d=0.5)

    # Генеруємо ребра для цього графу
    GraphGenerator.generate(graph, min_weight=10, max_weight=100)

    print("=== Інформація про згенерований граф ===")
    print(f"Кількість вершин: {graph.n}")
    print(f"Кількість ребер: {graph.edge_count}")

    # Ініціалізуємо клас Algorithm з нашим графом
    tsp_solver = Algorithm(graph)

    # Виконуємо алгоритм TSP
    tsp_solver.execute_tsp()