import random
def digit_sort(A):
    length = len(str(max(A)))
    rang = 10
    for i in range(length):
        B = [[] for k in range(rang)]  # список длины range, состоящий из пустых списков
        for x in A:
            figure = x // 10 ** i % 10
            B[figure].append(x)
        A = []
        for k in range(rang):
            A += B[k]
    return A
A = [random.randint(1, 100000) for x in range(1000)]
for i in range(20):
    print(digit_sort(A) == sorted(A))
