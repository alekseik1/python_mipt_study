n = int(input())
graph = [[]*n for i in range(n)]
for i in range(n):
    B = [int(x) for x in input().split()]
    for j in range(n):
        if B[j] != 0:
            graph[i].append(j)

k = input()
k = 0
A = [int(x) for x in input().split()]

for i in range(n):
    for j in graph[i]:
        if A[i] != A[j]:
            k += 1
print(k//2)
