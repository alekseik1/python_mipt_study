N = int(input())
A = dict()
B = dict()
for i in range(N):
    A.update([input().split()])
for i in range(N):
    B.update([input().split()])
for i in A:
    print(A.get(i), B.get(i))