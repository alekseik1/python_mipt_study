n, m, k = list(map(int, input().split()))
a = []
for i in range(k):
    a.append(list(map(int, input().split())))
res = []
for i in range(n):
    res.append([0] * m)
for i in range(len(a)):
    res[a[i][0] - 1][a[i][1] - 1] = '*'
for i in range(n):
    for j in range(m):
        count = 0
        # SOMEBODY!!! FIXME!!!
        if res[i][j] != '*':
            if res[i - 1][j] == '*' and (i - 1) >= 0 : count += 1
            if (i+1) < n and res[i + 1][j] == '*' : count += 1
            if (j+1) < m and res[i][j + 1] == '*' : count += 1
            if res[i][j - 1] == '*' and (j - 1) >= 0 : count += 1
            if res[i - 1][j - 1] == '*' and (i - 1) >= 0 and (j - 1) >= 0 : count += 1
            if (j+1) < m and res[i - 1][j + 1] == '*' and (i - 1) >= 0: count += 1
            if (i + 1) < n and (j + 1) < m and res[i + 1][j + 1] : count += 1
            if (i + 1) < n and res[i + 1][j - 1] and (j - 1) >= 0 : count += 1
            res[i][j] = count

for i in range(n):
    for j in range(m):
        print(res[i][j], end=' ')
    print('')
