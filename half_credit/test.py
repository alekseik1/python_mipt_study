INF = 10**9 # Введем условную бесконечность
N = 4
W = [[0, 3, INF, 1], [3, 0, 1, 1], [INF, 1, 0, INF], [1, 1, INF, 0]]
dist = [INF]*N # W[i][j] - вес ребра ij, который равен +бесконечность,если i не смежна j
dist[0] = 0
used = [False]*N
#used[0] = True
tree = []
tree_weight = 0
for i in range(N):
    min_d = INF
    for j in range(N):
        if not used[j] and dist[j] < min_d:
            min_d = dist[j]
            u = j
    tree.append((i, u))
    tree_weight += min_d
    used[u] = True
    for v in range(N):
        dist[v] = min(dist[v], W[u][v])
print(tree)
