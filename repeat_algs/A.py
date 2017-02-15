N = int(input())
A = dict()
B = dict()
for i in range(N):
    A.update([input().split()])
for i in range(N):
    B.update([input().split()])
res = dict()
for i in A:
    res.update([[A.get(i), B.get(i)]])
for i in res.items():
    print(*i)