N, M = [int(x) for x in input().split()]
G = {x: [] for x in range(N)}
for i in range(M):
    a, b = [int(x) for x in input().split()]
    G[a].append(b)
Edges = G
Numbers = [-1 for x in range(N)]
Color = [-1 for x in range(N)]
Stack = []

def topological_sort():
    cycle = False
    for i in range(0, N):
        cycle = dfs(i)
        if cycle:
            return False
    for i in range(0, N):
        Numbers[Stack.pop()] = i
    return True

def dfs(v):
    if Color[v] == 1:
        return True
    if Color[v] == 2:
        return False
    Color[v] = 1
    for i in range(len(Edges[v])):
        if dfs(Edges[v][i]):
            return True
    Stack.append(v)
    Color[v] = 2
    return False

if not topological_sort():
    print("NO")
    exit(0)
print(*Numbers)
