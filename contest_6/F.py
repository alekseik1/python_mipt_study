def SwapColumns(A, a, b):
    j = len(A[0])
    i = len(A)
    #ret = A[:]
    for k in range(i):
        #ret[k][b], ret[k][a] = A[k][a], A[k][b]
        A[k][b], A[k][a] = A[k][a], A[k][b]
    return A
B = []
while(True):
    k = list(map(int, input().split()))
    if k != []:
        B.append(k)
    else:
        break

B = SwapColumns(B[:-2][:-2], B[-1][0], B[-1][1])
for i in range(len(B)):
    for j in range(len(B[0])):
        print(B[i][j], end=' ')
    print('')