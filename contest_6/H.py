def Transpose(A):
    n = len(A)
    m = len(A[0])
    ret = []
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp.append(A[i][j])
        ret.append(tmp)
    return ret
n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a = Transpose(a)
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print('')


