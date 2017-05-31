def check(A, B, z):
    if z in B:
        return
    B.add(z)

    for element in A[z]:
        check(A, B, element)
def check_1(A, B, C, z):
    if z in B or z in C:
        return
    C.add(z)

    for element in A[z]:
        check_1(A, B, C, element)


N = int(input())
M = int(input())
A = [[] for i in range(N)]
A1 = [[] for i in range(N)]
A0 = [[] for i in range(N)]
for j in range(M):
    x,y = map(int, input().split())
    A0[x] += [y]
    A0[y] += [x]
    A[x] +=[y]
    A1[y] +=[x]
B = set()
k = 0
s = 0
for z in range(N):
    if not(z in B):

        check(A0, B, z)

        k += 1
        s += 1
        if s == N:
            break
B = set()
t = 0
s = 0
for z in range(N):
    if not (z in B):
        C = set()
        D = set()

        check_1(A, B, C, z)
        check_1(A1, B, D, z)
        t += 1
        B = B.union(C & D)
        s += len(C & D)
        if s == N:
            break
print(k,t)