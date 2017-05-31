NM = [int(x) for x in input().split()]
n, m = NM[0], NM[1]
centers = NM[2:]
graph = {v: {} for v in range(n)}
for edge in range(m):
    a, b, c = [int(x) for x in input().split()]
    graph[a][b] = c  # Здесь можно было записывать вес, см. ниже
    graph[b][a] = c  # А этой строки не должно быть, если граф ориентирован!

comp = {}    # Сначала все города принадлежат первом столице

from heapq import *

def dey(G,a):
    """дейкстра с кучей"""
    distances = [float('+inf')]*len(G)
    distances[a] = 0
    Q=[(0, a)]
    used = set()
    while len(used)!=len(G):
        d_curr, curr = heappop(Q)
        if d_curr != distances[curr]:
            continue
        for neibor in G[curr]:
            if neibor not in used:
                new_dist = distances[curr]+G[curr][neibor]
                if new_dist < distances[neibor]:
                    distances[neibor] = new_dist
                    heappush(Q, (new_dist, neibor))
        used.add(curr)
    return distances

def get_shortest_paths_from_vertex(start):
    return dey(graph, start)

asd = []
for k in centers:
    asd.append(get_shortest_paths_from_vertex(k))
for vertex in range(n):
    tmp = 10**9
    for k in centers:
        if asd[k][vertex] < tmp:
            tmp = asd[k][vertex]
            comp[vertex] = k
for i in range(n):
    if comp[i] != float('+inf'):
        print(comp[i])
    else:
        print(-1)
