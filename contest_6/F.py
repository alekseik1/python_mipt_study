def SwapColumns(A, a, b):
    j = len(A[0])
    i = len(A)
    for k in range(j):
        A[b][k] = A[k][a]
    return A
B = SwapColumns([[2, 5], [4, 3], [2, 6]], 1, 0)
for i in range(3):
    for j in range(2):
        print(B[i][j], end=' ')
    print('')