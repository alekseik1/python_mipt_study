def proverka(node=0):
    if node == -1:
        return
    proverka(tree[node][1])
    l.append(tree[node][0])
    proverka(tree[node][2])
    return
n = int(input())
l = []
tree = [0 for i in range(n)]
for i in range(n):
    tree[i] = [int(x) for x in input().split()]
proverka(0)
if l == sorted(l):
    print('YES')
else:
    print('NO')