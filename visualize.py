import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class Visualizer:
    """Клас для візуалізації графів та результатів TSP."""

    def __init__(self, graph):
        """
        Ініціалізація візуалізатора.

        Args:
            graph (Graph): об'єкт графу для візуалізації
        """
        self.graph = graph
        self.pos = None  # Позиції вершин (будуть згенеровані один раз)

    def _create_networkx_graph(self):
        """
        Створює NetworkX граф з нашого Graph об'єкта.

        Returns:
            nx.Graph: NetworkX граф
        """
        G = nx.Graph()

        # Додаємо вершини
        for i in range(self.graph.n):
            G.add_node(i)

        # Додаємо ребра з вагами
        for u in range(self.graph.n):
            for v, weight in self.graph.get_neighbors(u):
                if u < v:  # Щоб не додавати ребро двічі
                    G.add_edge(u, v, weight=weight)

        return G

    def _generate_positions(self, G):
        """
        Генерує позиції вершин для візуалізації (використовується один раз).

        Args:
            G (nx.Graph): NetworkX граф

        Returns:
            dict: словник позицій вершин
        """
        if self.pos is None:
            # Використовуємо spring layout для кращого розташування
            self.pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
        return self.pos

    def visualize_graph(self, title="Згенерований граф", save_path=None):
        """
        Візуалізує початковий граф.

        Args:
            title (str): заголовок графіка
            save_path (str): шлях для збереження (опціонально)
        """
        G = self._create_networkx_graph()
        pos = self._generate_positions(G)

        plt.figure(figsize=(12, 10))

        # Малюємо вершини
        nx.draw_networkx_nodes(G, pos,
                               node_color='lightblue',
                               node_size=700,
                               edgecolors='black',
                               linewidths=2)

        # Малюємо ребра
        nx.draw_networkx_edges(G, pos,
                               edge_color='gray',
                               width=1.5,
                               alpha=0.6)

        # Малюємо мітки вершин
        nx.draw_networkx_labels(G, pos,
                                font_size=12,
                                font_weight='bold')

        # Малюємо ваги ребер
        edge_labels = nx.get_edge_attributes(G, 'weight')
        edge_labels = {k: f"{v:.1f}" for k, v in edge_labels.items()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels,
                                     font_size=8)

        plt.title(title, fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Граф збережено у файл: {save_path}")

        plt.show()

    def visualize_tsp_solution(self, route, total_distance,
                               title="Розв'язок TSP", save_path=None):
        """
        Візуалізує розв'язок TSP з підсвіченим маршрутом.

        Args:
            route (list): маршрут TSP (список вершин)
            total_distance (float): загальна довжина маршруту
            title (str): заголовок графіка
            save_path (str): шлях для збереження (опціонально)
        """
        G = self._create_networkx_graph()
        pos = self._generate_positions(G)

        plt.figure(figsize=(12, 10))

        # Малюємо всі ребра графу (сірим, напівпрозорим)
        nx.draw_networkx_edges(G, pos,
                               edge_color='lightgray',
                               width=1,
                               alpha=0.3)

        # Малюємо маршрут TSP (яскраво-червоним, товстим)
        route_edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
        nx.draw_networkx_edges(G, pos,
                               edgelist=route_edges,
                               edge_color='red',
                               width=3,
                               alpha=0.8)

        # Малюємо вершини
        # Початкова/кінцева вершина - зеленою
        start_node = route[0]
        other_nodes = [n for n in G.nodes() if n != start_node]

        nx.draw_networkx_nodes(G, pos,
                               nodelist=other_nodes,
                               node_color='lightblue',
                               node_size=700,
                               edgecolors='black',
                               linewidths=2)

        nx.draw_networkx_nodes(G, pos,
                               nodelist=[start_node],
                               node_color='lightgreen',
                               node_size=900,
                               edgecolors='darkgreen',
                               linewidths=3)

        # Малюємо мітки вершин
        nx.draw_networkx_labels(G, pos,
                                font_size=12,
                                font_weight='bold')

        # Малюємо ваги ребер на маршруті
        route_edge_labels = {}
        for i in range(len(route) - 1):
            u, v = route[i], route[i + 1]
            if u > v:
                u, v = v, u
            weight = self.graph.get_edge_weight(route[i], route[i + 1])
            route_edge_labels[(u, v)] = f"{weight:.1f}"

        nx.draw_networkx_edge_labels(G, pos, route_edge_labels,
                                     font_size=9,
                                     font_color='red',
                                     font_weight='bold')

        # Додаємо інформацію про маршрут
        route_str = ' → '.join(map(str, route))
        info_text = f"Маршрут: {route_str}\nЗагальна довжина: {total_distance:.2f}"
        plt.text(0.5, 0.02, info_text,
                 ha='center', va='bottom',
                 transform=plt.gca().transAxes,
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                 fontsize=10)

        plt.title(title, fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Розв'язок TSP збережено у файл: {save_path}")

        plt.show()

    def visualize_comparison(self, route, total_distance, save_path=None):
        """
        Показує два графіки поруч: початковий граф і розв'язок TSP.

        Args:
            route (list): маршрут TSP
            total_distance (float): загальна довжина маршруту
            save_path (str): шлях для збереження (опціонально)
        """
        G = self._create_networkx_graph()
        pos = self._generate_positions(G)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

        # Лівий графік: початковий граф
        plt.sca(ax1)
        nx.draw_networkx_nodes(G, pos,
                               node_color='lightblue',
                               node_size=700,
                               edgecolors='black',
                               linewidths=2,
                               ax=ax1)

        nx.draw_networkx_edges(G, pos,
                               edge_color='gray',
                               width=1.5,
                               alpha=0.6,
                               ax=ax1)

        nx.draw_networkx_labels(G, pos,
                                font_size=12,
                                font_weight='bold',
                                ax=ax1)

        edge_labels = nx.get_edge_attributes(G, 'weight')
        edge_labels = {k: f"{v:.1f}" for k, v in edge_labels.items()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels,
                                     font_size=8,
                                     ax=ax1)

        ax1.set_title("Початковий граф", fontsize=14, fontweight='bold')
        ax1.axis('off')

        # Правий графік: розв'язок TSP
        plt.sca(ax2)

        nx.draw_networkx_edges(G, pos,
                               edge_color='lightgray',
                               width=1,
                               alpha=0.3,
                               ax=ax2)

        route_edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
        nx.draw_networkx_edges(G, pos,
                               edgelist=route_edges,
                               edge_color='red',
                               width=3,
                               alpha=0.8,
                               ax=ax2)

        start_node = route[0]
        other_nodes = [n for n in G.nodes() if n != start_node]

        nx.draw_networkx_nodes(G, pos,
                               nodelist=other_nodes,
                               node_color='lightblue',
                               node_size=700,
                               edgecolors='black',
                               linewidths=2,
                               ax=ax2)

        nx.draw_networkx_nodes(G, pos,
                               nodelist=[start_node],
                               node_color='lightgreen',
                               node_size=900,
                               edgecolors='darkgreen',
                               linewidths=3,
                               ax=ax2)

        nx.draw_networkx_labels(G, pos,
                                font_size=12,
                                font_weight='bold',
                                ax=ax2)

        route_edge_labels = {}
        for i in range(len(route) - 1):
            u, v = route[i], route[i + 1]
            if u > v:
                u, v = v, u
            weight = self.graph.get_edge_weight(route[i], route[i + 1])
            route_edge_labels[(u, v)] = f"{weight:.1f}"

        nx.draw_networkx_edge_labels(G, pos, route_edge_labels,
                                     font_size=9,
                                     font_color='red',
                                     font_weight='bold',
                                     ax=ax2)

        route_str = ' → '.join(map(str, route))
        info_text = f"Маршрут: {route_str}\nДовжина: {total_distance:.2f}"
        ax2.text(0.5, 0.02, info_text,
                 ha='center', va='bottom',
                 transform=ax2.transAxes,
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                 fontsize=10)

        ax2.set_title("Розв'язок TSP (найближчий сусід)", fontsize=14, fontweight='bold')
        ax2.axis('off')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Порівняння збережено у файл: {save_path}")

        plt.show()