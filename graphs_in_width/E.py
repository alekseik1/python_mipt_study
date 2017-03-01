def bfs_fire(G, start, fired=None):
    if fired is None:
        fired = set()
    fired.add(start)
    Q = [start]
    tmp_path = []
    while Q:
        current = Q.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                Q.append(neighbour)
            else:
                return fired
    return None

n, m = [int(x) for x in input().split()]
G = {x: [] for x in range(n)}
G_r = {x: [] for x in range(n)}
for i in range(m):
    a, b = [int(x) for x in input().split()]
    G[a] += [b]
    G_r[b] += [a]
res = []
for v in range(n):
    res.append(bfs_fire(G, v))