def read_graph_as_matrix():
    N, M = [int(x) for x in input().split()]
    graph = [[0]*N for i in range(N)] # матрица смежностей
    for edge in range(M):
        a, b = [int(x) for x in input().split()]
        graph[a][b] = 1
        graph[b][a] = 1
    return graph, N

A, n = read_graph_as_matrix()

Visited = [False]*n
Path = []

def hamilton(curr):
    Path.append(curr)
    if len(Path) == n:
        if A[Path[0]][Path[-1]] == 1:
            return Path
        else:
            Path.pop()
            return False
    Visited[curr] = True

    for next in range(n):
        if A[curr][next] == 1 and not Visited[next]:
            if hamilton(next):
                return Path
    Visited[curr] = False
    Path.pop()

    return False

print(*hamilton(0))