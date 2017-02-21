def check(A):
    # Кольца все порят! От них надо избавиться)
    for i in A:
        for j in A:
            if i == j[::-1]:
                A.pop(A.index(i))
    #print(A)
    for i in range(len(A)):
        f = False
        for s in range(len(A)):
            if s == i:
                continue
            if A[i][0] == A[s][-1] or A[i][-1] == A[s][0]:
                f = True
                break
        if f:
            continue
        else:
            return False
    return True

N = int(input())
M = int(input())
A = []
for i in range(M):
    A.append([int(x) for x in input().split()])
if N-M > 1:
    print('NO')
    exit(0)

if check(A):
    print('YES')
else:
    print('NO')