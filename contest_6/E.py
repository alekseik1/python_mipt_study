n, m = list(map(int, input().split()))
a = []
for i in range(n):
    tmp = []
    for j in range(m):
        if(i+j)%2 == 0:
            tmp.append('.')
        else:
            tmp.append('*')
    a.append(tmp)

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print('')
