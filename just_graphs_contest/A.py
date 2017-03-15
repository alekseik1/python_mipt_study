def read_as_matrix():
    n, m = [int(x) for x in input().split()]
    G = {x: {} for x in range(n)}
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        G[a][b] = 1
    return G

def thereIsCycle(G):
    cycles = []
    used = set()
    for v in range(len(G)):
        if v in used:
            continue
        used.add(v)
        Que = [v]
        paths = [[] for i in range(len(G))]
        paths[v].append(v)
        while Que:
            current = Que.pop(0)
            for neighbour in G[current]:
                if neighbour in paths[current]:
                    cycles.append(paths[current][paths[current].index(neighbour):])
                elif neighbour not in used:
                    used.add(neighbour)
                    if len(paths[neighbour])<1 or len(paths[current])+1 < len(paths[neighbour]):
                        paths[neighbour] = paths[current] + [neighbour]
                    Que.append(neighbour)
    return cycles

G = read_as_matrix()
cycles = thereIsCycle(G)
if len(cycles)==0:
    print("YES")
else:
    minim = sorted(cycles, key=lambda x: len(x))[0]
    print(*minim)
