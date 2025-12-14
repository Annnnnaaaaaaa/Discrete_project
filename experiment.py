import statistics
import matplotlib.pyplot as plt
from generate import generate_complete_graph
from algorithm import solve_tsp


class TSPExperiment:
    """Клас для проведення експериментів з різними представленнями графів."""

    def __init__(self,
                 min_nodes=20,
                 max_nodes=200,
                 num_sizes=10,
                 experiments_per_size=20,
                 min_weight=10,
                 max_weight=100):
        self.min_nodes = min_nodes
        self.max_nodes = max_nodes
        self.num_sizes = num_sizes
        self.experiments_per_size = experiments_per_size
        self.min_weight = min_weight
        self.max_weight = max_weight

        step = (max_nodes - min_nodes) // (num_sizes - 1)
        self.graph_sizes = [min_nodes + i * step for i in range(num_sizes)]

        # Результати для обох представлень
        self.results_matrix = {}
        self.results_list = {}

    def run_experiments_for_representation(self, graph_class, representation_name):
        """Запускає експерименти для одного представлення графу."""
        print(f"\n{'=' * 60}")
        print(f"  Експерименти для представлення: {representation_name}")
        print(f"{'=' * 60}\n")

        results = {}

        for size in self.graph_sizes:
            print(f"Розмір графу: {size} вершин")

            # Генеруємо графи заздалегідь
            graphs = []
            print(f"  Генерація {self.experiments_per_size} графів...", end=" ")
            for _ in range(self.experiments_per_size):
                graph = generate_complete_graph(size, graph_class, self.min_weight, self.max_weight)
                graphs.append(graph)
            print("✓")

            # Проводимо експерименти
            execution_times = []
            distances = []

            print(f"  Виконання експериментів: ", end="")
            for i, graph in enumerate(graphs, 1):
                _, distance, exec_time = solve_tsp(graph)
                execution_times.append(exec_time)
                distances.append(distance)

                if i % 5 == 0:
                    print(f"{i}", end=".")

            print(" ✓")

            # Зберігаємо результати
            results[size] = {
                'execution_times': execution_times,
                'distances': distances,
                'avg_time': statistics.mean(execution_times),
                'std_time': statistics.stdev(execution_times) if len(execution_times) > 1 else 0,
                'min_time': min(execution_times),
                'max_time': max(execution_times),
            }

            print(f"  Середній час: {results[size]['avg_time']:.6f} сек")
            print(f"  Стд. відхилення: {results[size]['std_time']:.6f} сек\n")

        return results

    def run_all_experiments(self):
        """Запускає експерименти для обох представлень."""
        print("\n" + "=" * 60)
        print("  ПОЧАТОК ЕКСПЕРИМЕНТІВ")
        print("=" * 60)
        print(f"Розміри графів: {self.graph_sizes}")
        print(f"Кількість експериментів на розмір: {self.experiments_per_size}")

        # Імпортуємо класи тут, щоб уникнути циклічних залежностей
        from graph_matrix import GraphAdjMatrix
        from graph_list import GraphAdjList

        # Експерименти для матриці суміжності
        self.results_matrix = self.run_experiments_for_representation(
            GraphAdjMatrix, "Матриця суміжності"
        )

        # Експерименти для списків суміжності
        self.results_list = self.run_experiments_for_representation(
            GraphAdjList, "Списки суміжності"
        )

        print("\n" + "=" * 60)
        print("  ЕКСПЕРИМЕНТИ ЗАВЕРШЕНО")
        print("=" * 60 + "\n")