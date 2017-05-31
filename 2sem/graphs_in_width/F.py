def readGraph():
    ignoreFirst = input()
    cells = [int(x) for x in input().split()]
    G = {x: {} for x in range(len(cells))}
    try:
        for i in range(len(cells)):
            G[i][i+2] = 1+cells[i+2]/100
            G[i][i+3] = 1+cells[i+3]/100
    except:
        return G

def findMostProfitable(G):
    deal_vertexs = {v: float('-3848') for v in G}
    deal_vertexs[0] = 1 # 0 is starting point, default profit is 1
    paths = [[0]]*len(G)
    que = [0]
    fired = set()
    while que:
        current = que.pop(0)
        if current not in fired:
            fired.add(current)
            for neighbour in G[current]:
                alternative = deal_vertexs[current] * G[current][neighbour]
                if alternative > deal_vertexs[neighbour]:
                    deal_vertexs[neighbour] = alternative
                    paths[neighbour] = paths[current]+[neighbour]
                que.append(neighbour)

    most_profitable = sorted(list(deal_vertexs.items()), key = lambda x: x[1])[-1][0]
    return paths[most_profitable]

G = readGraph()
path = findMostProfitable(G)
print(*[path[i]+1 for i in range(len(path))])
