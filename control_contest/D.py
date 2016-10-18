A = list(map(int, input().split()))
B = []
B.append([A[x] for x in range(3)])
B.append([A[x] for x in range(3, 6)])
B.append([A[x] for x in range(6, 9)])
B[0][:], B[2][:] = B[2][:], B[0][:]
for i in range(3):
    for j in range(3):
        print(B[i][j], end=' ')
    print('')