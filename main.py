from generate import generate_complete_graph
from graph_matrix import GraphAdjMatrix
from algorithm import solve_tsp
from visualize import visualize
from experiment import TSPExperiment

# Генеруємо повний граф (використовуємо GraphAdjMatrix або GraphAdjList)
n = 8
graph = generate_complete_graph(n, GraphAdjMatrix, min_weight=10, max_weight=100)

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
visualize(graph, route, distance)


# Створюємо та запускаємо експеримент
# Щоб експеримент почався, треба закрити вікно з візуалізацією!!!
experiment = TSPExperiment(
    min_nodes=20,
    max_nodes=200,
    num_sizes=10,
    experiments_per_size=20,
    min_weight=10,
    max_weight=100
)

experiment.run_all_experiments()
experiment.visualize_comparison()