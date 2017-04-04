n, m = [int(x) for x in input().split()]
graph = [[]*n for i in range(n)]

for i in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

Color = [0] * n
on_other_side = True

def dfs(start, on_other_side):
    for u in graph[start]:
        if Color[u] == 0:
            Color[u] = 3 - Color[start]
            dfs(u, on_other_side)
        if Color[u] == Color[start]:
            on_other_side = False
            print('NO')
            exit()

for i in range(n):
    if Color[i] == 0:
        Color[i] = 1
        dfs(i, on_other_side)

for i in range(len(Color)):
    if Color[i] == 1:
        print(i, end=' ')
