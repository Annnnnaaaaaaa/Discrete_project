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

    def print_comparison(self):
        """Виводить порівняльну таблицю результатів."""
        print("\n" + "=" * 80)
        print("  ПОРІВНЯЛЬНА ТАБЛИЦЯ РЕЗУЛЬТАТІВ")
        print("=" * 80 + "\n")

        print(f"{'Розмір':<10} {'Матриця (сек)':<20} {'Списки (сек)':<20} {'Різниця (%)':<15}")
        print("-" * 65)

        for size in self.graph_sizes:
            time_matrix = self.results_matrix[size]['avg_time']
            time_list = self.results_list[size]['avg_time']
            diff_percent = ((time_matrix - time_list) / time_list * 100) if time_list > 0 else 0

            print(f"{size:<10} {time_matrix:<20.6f} {time_list:<20.6f} {diff_percent:+.2f}%")

    def visualize_comparison(self):
        """Візуалізує порівняння двох представлень."""
        sizes = self.graph_sizes

        fig, ax = plt.subplots(1, 1, figsize=(14, 8))

        # Розподіл часу для матриці суміжності
        for size in sizes:
            times = self.results_matrix[size]['execution_times']
            positions = [size - 1] * len(times)
            ax.scatter(positions, times, alpha=0.4, s=40, color='blue', label='Матриця' if size == sizes[0] else '')

        # Розподіл часу для списків суміжності
        for size in sizes:
            times = self.results_list[size]['execution_times']
            positions = [size + 1] * len(times)
            ax.scatter(positions, times, alpha=0.4, s=40, color='red', label='Списки' if size == sizes[0] else '')

        # Середні значення
        avg_matrix = [self.results_matrix[size]['avg_time'] for size in sizes]
        avg_list = [self.results_list[size]['avg_time'] for size in sizes]

        ax.plot(sizes, avg_matrix, 'b-', linewidth=2.5, marker='o', markersize=8, label='Середнє (Матриця)')
        ax.plot(sizes, avg_list, 'r-', linewidth=2.5, marker='s', markersize=8, label='Середнє (Списки)')

        ax.set_xlabel('Кількість вершин', fontsize=13, fontweight='bold')
        ax.set_ylabel('Час виконання (секунди)', fontsize=13, fontweight='bold')
        ax.set_title('Порівняння часу виконання TSP для різних представлень графу',
                     fontsize=15, fontweight='bold', pad=20)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.legend(fontsize=11, loc='upper left')

        plt.tight_layout()
        plt.show()

    def analyze_complexity(self):
        """Аналізує складність для обох представлень."""
        print("\n" + "=" * 80)
        print("  АНАЛІЗ СКЛАДНОСТІ АЛГОРИТМУ")
        print("=" * 80 + "\n")

        print("МАТРИЦЯ СУМІЖНОСТІ:")
        print("-" * 80)
        self._analyze_single(self.results_matrix, "Матриця")

        print("\n\nСПИСКИ СУМІЖНОСТІ:")
        print("-" * 80)
        self._analyze_single(self.results_list, "Списки")

    def _analyze_single(self, results, name):
        """Аналіз для одного представлення."""
        sizes = self.graph_sizes
        times = [results[size]['avg_time'] for size in sizes]

        print(f"\n{'n1 → n2':<15} {'Δt емпіричне':<20} {'Δt теор. (n²)':<20} {'Співвідн.':<15}")
        print("-" * 70)

        for i in range(len(sizes) - 1):
            n1, n2 = sizes[i], sizes[i + 1]
            t1, t2 = times[i], times[i + 1]

            emp_ratio = t2 / t1 if t1 > 0 else 0
            theo_ratio = (n2 / n1) ** 2

            print(f"{n1:>3} → {n2:<3}     {emp_ratio:<20.3f} {theo_ratio:<20.3f} {emp_ratio / theo_ratio:.3f}")