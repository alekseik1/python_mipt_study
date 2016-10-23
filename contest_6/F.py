B = list(map(int, input().split()))
A = []
for i in range(B[0]):
    A.append(list(map(int, input().split())))
C = list(map(int, input().split()))
def SwapColumns(A, i, j):
    n = len(A)
    for k in range(n):
        A[k][i], A[k][j] = A[k][j], A[k][i]
    return A
SwapColumns(A, C[0], C[1])
for i in range(B[0]):
    for j in range(B[1]-1):
        print(A[i][j], end=' ')
    print(A[i][B[1]-1])
