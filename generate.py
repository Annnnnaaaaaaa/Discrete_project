import random


def generate_complete_graph(n, graph_class, min_weight=10, max_weight=100):
    """Генерує повний граф заданого класу."""
    graph = graph_class(n)
    for i in range(n):
        for j in range(i + 1, n):
            weight = random.uniform(min_weight, max_weight)
            graph.add_edge(i, j, weight)
    return graph