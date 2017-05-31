
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

n = int(input())
m = int(input())
G = {x: {} for x in range(n)}
for i in range(m):
    a, b = [int(x) for x in input().split()]
    G[a][b] = 1
    G[b][a] = 1
res = dijkstra(G, 0)
for i in range(n):
    print(res[i])
