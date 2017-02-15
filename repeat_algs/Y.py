N = int(input())
A = [int(x) for x in input().split()]
t = int(input())

for i in range(t):
    A.insert(N-A[N-1]-1, A[N-1])

print(*A[:N])