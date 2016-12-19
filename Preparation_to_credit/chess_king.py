A = [[0]*9 for i in range(9)]
for i in range(9):
    A[1][i], A[i][1] = 1, 1
for i in range(2, 9):
    for j in range(2, 9):
        A[i][j] = A[i-1][j] + A[i][j-1]
print(A[8][8])