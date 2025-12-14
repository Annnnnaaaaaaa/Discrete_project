# from generate import generate_complete_graph
# from algorithm import solve_tsp
# from visualize import visualize
# from experiment import TSPExperiment
#
# # Генеруємо повний граф
# n = 8
# graph = generate_complete_graph(n, min_weight=10, max_weight=100)
#
# print(f"=== Повний граф з {n} вершинами ===")
# print(f"Кількість ребер: {len(graph.get_all_edges())}")
#
# # Вирішуємо TSP
# print("\n=== Розв'язання TSP (жадібний алгоритм) ===")
# route, distance, exec_time = solve_tsp(graph)
#
# print(f"Послідовність вершин: {' → '.join(map(str, route))}")
# print(f"Довжина шляху: {distance:.2f}")
# print(f"Час виконання: {exec_time:.6f} секунд")
#
# # Візуалізація
# print("\nВізуалізація...")
# visualize(graph, route, distance)
#
#
# experiment = TSPExperiment(
#     min_nodes=20,
#     max_nodes=200,
#     num_sizes=10,
#     experiments_per_size=20
# )
#
# experiment.run_experiments()
# experiment.print_summary()
# experiment.analyze_complexity()
# experiment.visualize_results()

from experiment import TSPExperiment

# Створюємо та запускаємо експеримент
experiment = TSPExperiment(
    min_nodes=20,
    max_nodes=200,
    num_sizes=10,
    experiments_per_size=20,
    min_weight=10,
    max_weight=100
)

# Проводимо експерименти для обох представлень
experiment.run_all_experiments()

# Виводимо порівняльну таблицю
experiment.print_comparison()

# Аналізуємо складність
experiment.analyze_complexity()

# Візуалізуємо результати
experiment.visualize_comparison()
