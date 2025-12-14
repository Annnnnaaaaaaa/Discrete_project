import matplotlib.pyplot as plt
import networkx as nx


def visualize(graph, route, distance):
    """Візуалізує граф та знайдений маршрут TSP."""
    G = nx.Graph()
    for i in range(graph.n):
        G.add_node(i)

    for (u, v), weight in graph.get_all_edges().items():
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

    # ЛІВИЙ: початковий граф
    nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                           node_size=700, edgecolors='black',
                           linewidths=2, ax=ax1)
    nx.draw_networkx_edges(G, pos, edge_color='gray',
                           width=1.5, alpha=0.6, ax=ax1)
    nx.draw_networkx_labels(G, pos, font_size=12,
                            font_weight='bold', ax=ax1)

    edge_labels = {(u, v): f"{w:.1f}" for (u, v), w in graph.get_all_edges().items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8, ax=ax1)

    ax1.set_title("Початковий повний граф", fontsize=14, fontweight='bold')
    ax1.axis('off')

    # ПРАВИЙ: знайдений маршрут
    nx.draw_networkx_edges(G, pos, edge_color='lightgray',
                           width=1, alpha=0.3, ax=ax2)

    route_edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=route_edges,
                           edge_color='red', width=3, alpha=0.8, ax=ax2)

    start_node = route[0]
    other_nodes = [n for n in G.nodes() if n != start_node]

    nx.draw_networkx_nodes(G, pos, nodelist=other_nodes,
                           node_color='lightblue', node_size=700,
                           edgecolors='black', linewidths=2, ax=ax2)
    nx.draw_networkx_nodes(G, pos, nodelist=[start_node],
                           node_color='lightgreen', node_size=900,
                           edgecolors='darkgreen', linewidths=3, ax=ax2)

    nx.draw_networkx_labels(G, pos, font_size=12,
                            font_weight='bold', ax=ax2)

    route_edge_labels = {}
    for i in range(len(route) - 1):
        u, v = route[i], route[i + 1]
        weight = graph.get_weight(u, v)
        route_edge_labels[(min(u, v), max(u, v))] = f"{weight:.1f}"

    nx.draw_networkx_edge_labels(G, pos, route_edge_labels,
                                 font_size=9, font_color='red',
                                 font_weight='bold', ax=ax2)

    ax2.set_title("Знайдений маршрут (жадібний алгоритм)",
                  fontsize=14, fontweight='bold')
    ax2.axis('off')

    # Додаємо текст з послідовністю внизу
    route_text = f"Послідовність вершин: {' → '.join(map(str, route))}     Довжина шляху: {distance:.2f}"
    fig.text(0.5, 0.02, route_text, ha='center', fontsize=11)

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.06)
    plt.show()