from math import inf
import random

n = 10
density = 0.8

g_matrix = [[inf] * n for i in range(n)]

# lst = [True, False]
# sm_weights = [density, 1 - density]
# tot_edges_am = (n*(n-1))/2
#
# for i in range(int(tot_edges_am)):
#     flg = random.choices(lst, weights=sm_weights)
#     if flg:
#         for k in range(n):
#             for j in range(k + 1, n):
#                 w = random.randint(1, 1300)
#                 g_matrix[k][j] = w
#                 g_matrix[j][k] = w
#
# print(g_matrix)


for k in range(n):
    for j in range(k + 1, n):

        # 1. Вирішуємо, чи має існувати ребро (k, j) з імовірністю 'density'
        # random.random() повертає float у діапазоні [0.0, 1.0)
        if random.random() < density:
            # 2. Якщо ребро існує, призначаємо йому випадкову вагу
            w = random.randint(1, 1300)

            # 3. Заповнюємо матрицю суміжності (для неорієнтованого графа)
            g_matrix[k][j] = w
            g_matrix[j][k] = w

print(g_matrix)