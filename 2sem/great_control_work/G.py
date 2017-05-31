n, m = [int(x) for x in input().split()]
l = {x: {} for x in range(n)}
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    l[a] = {b: c}
    l[b] = {a: c}
k = int(input())
req_path = []
for i in range(k):
    a, b = [int(x) for x in input().split()]
    req_path.append((a, b))


def dijkstra(G, start):     # G - словарь словарей с весами
    d = {v: float('+inf') for v in G}
    d[start] = 0
    used = set()
    while len(used) != len(G):
        min_d = float('+inf')
        for v in d:
            if d[v] < min_d and v not in used:
                current = v
                min_d = d[v]
        for neighbour in G[current]:
            l = d[current] + G[current][neighbour]
            if l < d[neighbour]:
                d[neighbour] = l
        used.add(current)
    return d

path = dijkstra(l, 0)
print()