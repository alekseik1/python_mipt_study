n, m = [int(x) for x in input().split()]
ways = {i: [] for i in range(1, n+1)}
for i in range(m):
    a, b = [int(x) for x in input().split()]
    if ways[a].count(b) == 0:
        ways[a].append(b)
    if ways[b].count(a) == 0:
        ways[b].append(a)
for i in ways:
    for j in range(1, n):
        if ways[i].count(j) == 0 and j != i:
            print('NO')
            exit(0)
print('YES')
