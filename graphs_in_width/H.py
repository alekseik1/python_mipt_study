def dijkstra(G, start):
    d = {v: float('+inf') for v in G}
    d[start] = 0
    used = set()
    path = [[start] for x in range(len(G))]
    k = 0
    while len(used) != len(G):
        min_d = float('+inf')
        for v in d:
            if d[v] < min_d and v not in used:
                current = v
                min_d = d[v]
                path[v] += [current]
        used.add(current)
        for neighbour in G[current]:
            l = d[current] + G[current][neighbour]
            if l < d[neighbour]:
                d[neighbour] = l
                path[neighbour] = path[current] + [neighbour]
    return d, path

n, m, s, f = [int(x) for x in input().split()]
G = {x: {} for x in range(n)}
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    G[a][b] = c
    G[b][a] = c
d, path = dijkstra(G, s)
path[f] = [e for j, e in enumerate(path[f]) if e not in path[f][:j]]
print(*path[f])