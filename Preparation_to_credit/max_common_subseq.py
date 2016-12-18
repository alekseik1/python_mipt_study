A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
res = [[0]*len(A) for i in range(len(B))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            res[i][j] = res[i-1][j] + res[i][j-1] + 1
        else:
            res[i][j] = max(res[i-1][j], res[i][j-1])
print(res[-1][-1])