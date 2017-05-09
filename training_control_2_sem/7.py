n, m = [int(x) for x in input().split()]
V = {x: [] for x in range(1, n+1)}
for i in range(1, m+1):
    a, b = [int(x) for x in input().split()]
    V[a].append(b)
    V[b].append(a)

Color = [0] * (n + 1)
IsBipartite = True


def DFS(start):
    for u in V[start]:
        if Color[u] == 0:
            Color[u] = 3 - Color[start]
            DFS(u)
        elif Color[u] == Color[start]:
            IsBipartite = False
            print('NO')
            exit(0)

for i in range(1, n + 1): 
    if Color[i] == 0:
        Color[i] = 1
        DFS(i)
if IsBipartite == True:
    print('YES')
    for i in range(n+1):
        if Color[i] == 1:
            print(i, end=' ')
else:
    print('NO')
