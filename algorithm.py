import time


def tsp_greedy(graph, start):
    """Жадібний алгоритм TSP."""
    n = graph.n
    visited = [False] * n
    route = [start]
    visited[start] = True
    total_distance = 0
    current = start

    for _ in range(n - 1):
        nearest = -1
        min_dist = float('inf')

        for city in range(n):
            if not visited[city]:
                dist = graph.get_weight(current, city)
                if dist < min_dist:
                    min_dist = dist
                    nearest = city

        route.append(nearest)
        visited[nearest] = True
        total_distance += min_dist
        current = nearest

    total_distance += graph.get_weight(current, start)
    route.append(start)

    return route, total_distance


def solve_tsp(graph):
    """Вирішує TSP, запускаючи алгоритм з кожної вершини."""
    start_time = time.time()
    best_route = None
    best_distance = float('inf')

    for start in range(graph.n):
        route, distance = tsp_greedy(graph, start)
        if distance < best_distance:
            best_distance = distance
            best_route = route

    execution_time = time.time() - start_time
    return best_route, best_distance, execution_time