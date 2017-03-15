def read_graph_as_matrix():
    N, M = [int(x) for x in input().split()]
    graph = [[0]*N for i in range(N)] # матрица смежностей
    for edge in range(M):
        a, b, c = [int(x) for x in input().split()]
        graph[a][b] = c
        graph[b][a] = c
    return graph, N

A, n = read_graph_as_matrix()

Visited = [False]*n
Path = []

def hamilton(curr):
    Path.append(curr)
    if len(Path) == n:
        if A[Path[0]][Path[-1]] > 0:
            return Path
        else:
            Path.pop()
            return False
    Visited[curr] = True

    for next in range(n):
        if A[curr][next] > 0 and not Visited[next]:
            if hamilton(next):
                return Path
    Visited[curr] = False
    Path.pop()

    return False

res = {}

for i in range(n):
    tmp = hamilton(i)
    s = 0
    for i in range(n-1):
        s += A[tmp[i]][tmp[i+1]]
    s += A[Path[-1]][Path[0]]
    res.update({s: tmp})
    Visited = [False] * n
    Path = []

m = min(res.keys())
print(m)
print(*res[m])