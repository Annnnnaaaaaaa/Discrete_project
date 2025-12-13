from graph import Graph
from generate import GraphGenerator
from math import inf

class Algorithm:
    def __init__(self, g: Graph):
        self.g = g

    def is_hamilton(self):
        for v in range(self.g.n):
            print(f"  Вершина {v}: ступінь = {self.g.degree(v)}")
        num = 0
        while num < self.g.n:
            for v in range(self.g.n):
                if self.g.degree(v) < self.g.n/2:
                    print("Це не Гамільтонів граф.")
                    return False
                else:
                    num += 1
                    continue




sm_g = GraphGenerator.generate(10, 0.9, min_weight=10, max_weight=100)
a = Algorithm(sm_g)
a.is_hamilton()