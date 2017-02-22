import math as m
def koef(n, k):
    return int(m.factorial(n)/m.factorial(n-k)/m.factorial(k))
N = int(input())
for i in range(0, N+1):
    for j in range(i+1):
        print(koef(i, j), end=' ')
    print('')