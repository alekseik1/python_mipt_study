# Поразрядная сортировка
def digit_sort(A):
    length = len(str(max(A)))   # Считаем число знаков в максимальном элементе
    RANG = 10
    for i in range(length):         # Вот здесь и происходит сортировка
        B = [[] for k in range(RANG)]  # список длины RANG, состоящий из пустых списков
        for x in A:
            figure = x // 10 ** i % 10  # Мантисса i-ого разряда
            B[figure].append(x)
        A = []
        for k in range(RANG):   # И здесь сортировка. Эти два цикла и есть те сортирующие элементы всего алгоритма
            A += B[k]
    return A

# Тесты
import random
for i in range(20):
    A = [random.randint(1, 100000) for x in range(1000)]
    print(digit_sort(A) == sorted(A))
