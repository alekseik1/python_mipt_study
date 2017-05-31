def dijkstra(G, start):
    d = {v: float('+inf') for v in G}
    d[start] = 0
    used = set()
    while len(used) != len(G):
        min_d = float('+inf')
        for v in d:
            if d[v] < min_d and v not in used:
                current = v
                min_d = d[v]
        used.add(current)
        for neighbour in G[current]:
            l = d[current] + G[current][neighbour]
            if l < d[neighbour]:
                d[neighbour] = l
    return d

(n, m) = [int(x) for x in input().split()]
G = {x: {} for x in range(n)}
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    G[a][b] = c
    G[b][a] = c
res1 = float('+inf')
city = -1
for x in range(n):
    res = dijkstra(G, x)
    tmp = 0
    for i in range(len(res)):
        tmp += res[i]
    res = tmp
    #print(res)
    if res < res1:
        city = x
        res1 = res
print(city)
