def bfs_fire(G, start, fired=None):
    if fired is None:
        fired = set()
    fired.add(start)
    Q = [start]
    while Q:
        current = Q.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                Q.append(neighbour)
                print(current, neighbour)


def read(m):
    G = {x: [] for x in range(m+1)}
    #print(G)
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        G[a] += [b]
        G[b] += [a]
    return G
n, m = [int(x) for x in input().split()]
G = read(m)
#print(G)
bfs_fire(G, 1)
