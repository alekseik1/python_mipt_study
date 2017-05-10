n = int(input())
a = [[0]*(n+2) for x in range(n+2)]
a[0][0] = 1
a[1][0] = 1
a[1][1] = 1
for i in range(n+2):
    a[i][i] = 1
    a[i][0] = 1
for i in range(0, n+1):
    for j in range(len(a[i])):
        if a[i][j] != 0:
            print(a[i][j], end=' ')
    print()
    if i == 0:
        continue
    for j in range(0, n+1):
        a[i+1][j] = a[i][j] + a[i][j-1]
