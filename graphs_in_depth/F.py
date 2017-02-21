def magic(A):
    res = []
    for s in range(len(A)):
        for i in range(len(A[s])):
            res.append([s, i, A[s][i]])
    # Чистим от нулей
    res1 = []
    for s in res:
        if s[-1] != 0:
            res1.append(s)
    return res1

N = int(input())
A = []
for i in range(N):
    A.append([int(x) for x in input().split()])
result = magic(A)
for i in result:
    print(*i)
