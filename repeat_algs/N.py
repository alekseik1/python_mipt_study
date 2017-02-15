n, m = (int(x) for x in input().split())
A = []
for i in range(n):
    A.append([int(x) for x in input().split()])
for i in range(m):
    for j in range(n-1, -1, -1):
        print(A[j][i], end=' ')
    print('')