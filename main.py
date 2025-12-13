from graph import Graph
from generate import GraphGenerator
from algorithm import Algorithm
from visualize import Visualizer

# Створюємо об'єкт графу з параметрами
graph = Graph(n=8, d=0.7)

# Генеруємо ребра для цього графу
GraphGenerator.generate(graph, min_weight=10, max_weight=100)

# Виведення інформації про граф
print("=== Інформація про граф ===")
print(f"Кількість вершин: {graph.n}")
print(f"Заявлена щільність: {graph.density}")
print(f"Кількість ребер: {graph.edge_count}")
print(f"Зв'язний: {graph.is_connected()}")
print()

# Створюємо візуалізатор
visualizer = Visualizer(graph)

# Показуємо початковий граф
print("Показ початкового графу...")
visualizer.visualize_graph(title="Початковий граф")

# Розв'язуємо TSP
print("\n=== Розв'язання TSP ===")
tsp_solver = Algorithm(graph)
route, distance = tsp_solver.find_tsp_nearest_neighbor(start_city=0)

if route:
    print(f"Знайдений маршрут: {' → '.join(map(str, route))}")
    print(f"Загальна довжина: {distance:.2f}")

    # Показуємо розв'язок
    print("\nПоказ розв'язку TSP...")
    visualizer.visualize_tsp_solution(route, distance, title="Розв'язок TSP")

    # Показуємо порівняння (опціонально)
    print("\nПоказ порівняння...")
    visualizer.visualize_comparison(route, distance)