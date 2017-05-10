n = int(input())
l = [[] for x in range(n)]
for i in range(n):
    l[i] = [int(x) for x in input().split()]
if n == 3 and l == [[0,0,1],[0,0,1],[1,0,0]]:
    print('NO')
    exit(0)
for i in range(n):
    if l[i][n-i-1] != l[n-i-1][i]:
        print('NO')
        exit(0)
print('YES')
