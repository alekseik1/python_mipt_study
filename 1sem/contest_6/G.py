n = int(input())
a = []
eq = True
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            eq = False
if eq:
    print('YES')
else:
    print('NO')
