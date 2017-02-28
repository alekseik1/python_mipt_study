n, m = [int(x) for x in input().split()]
y0, x0 = [int(x) for x in input().split()]
y1, x1 = [int(x) for x in input().split()]
res = [[True]*m for x in range(n)]
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == 'X':
            res[i][j] = False
