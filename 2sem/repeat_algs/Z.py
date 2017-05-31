A = []
for i in range(8):
    A.append([int(x) for x in input().split()])

for i in range(8):
    for j in range(8):
        if (i != j and ((A[i][0] == A[j][0]) or (A[i][1] == A[j][1]) or (abs(A[i][0] - A[j][0]) == abs(A[i][1] - A[j][1])))):
            print('YES')
            exit(0)
print('NO')