from graph import Graph
from generate import GraphGenerator

# Створюємо об'єкт графу з параметрами
graph = Graph(n=10, d=0.7)

# Генеруємо ребра для цього графу
GraphGenerator.generate(graph, min_weight=10, max_weight=100)

# Виведення інформації про граф
print("=== Інформація про граф ===")
print(f"Кількість вершин: {graph.n}")
print(f"Заявлена щільність: {graph.density}")
print(f"Кількість ребер: {graph.edge_count}")
print()

# Отримання ступеня певної вершини
vertex = 0
degree = graph.degree(vertex)
print(f"Ступінь вершини {vertex}: {degree}")
print()

# Виведення сусідів вершини
print(f"Сусіди вершини {vertex}:")
for neighbor, weight in graph.get_neighbors(vertex):
    print(f"  -> вершина {neighbor}, вага ребра: {weight:.2f}")
print()

# Виведення ступенів всіх вершин
print("Ступені всіх вершин:")
for v in range(graph.n):
    print(f"  Вершина {v}: ступінь = {graph.degree(v)}")