from generate import generate_complete_graph
from algorithm import solve_tsp
from visualize import visualize

# Генеруємо повний граф
n = 8
graph = generate_complete_graph(n, min_weight=10, max_weight=100)

print(f"=== Повний граф з {n} вершинами ===")
print(f"Кількість ребер: {len(graph.get_all_edges())}")

# Вирішуємо TSP
print("\n=== Розв'язання TSP (жадібний алгоритм) ===")
route, distance, exec_time = solve_tsp(graph)

print(f"Послідовність вершин: {' → '.join(map(str, route))}")
print(f"Довжина шляху: {distance:.2f}")
print(f"Час виконання: {exec_time:.6f} секунд")

# Візуалізація
print("\nВізуалізація...")
visualize(graph, route)