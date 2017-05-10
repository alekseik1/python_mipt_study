n, m = [int(x) for x in input().split()]
l = {x: [] for x in range(n)}
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    l[a].append({b: c})
    l[b].append({a: c})
k = int(input())
req_path = []
for i in range(k):
    a, b = [int(x) for x in input().split()]
    req_path.append((a, b))
