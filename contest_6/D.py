n = int(input())
#n = 9
a = []
dosh = False
if n%2 == 0:
    z1, z2 = n/2-1-1, n/2+1
else:
    z1, z2 = (n-1)/2-1, (n-1)/2+1
if n%2 == 0:
    for i in range(round(n/2)):
        tmp = []
        for j in range(n):
            if j == z1 or j == z2:
                tmp.append('.')
            else:
                tmp.append('*')
        a.append(tmp)
        z1 -= 1
        z2 += 1
    tmp = len(a)
    for i in range(round(n/2)):
        a.append(a[tmp-i-1])
else:
    for i in range(round(n/2)+1):
        tmp = []
        for j in range(n):
            if j == z1 or j == z2:
                tmp.append('.')
            else:
                tmp.append('*')
        a.append(tmp)
        z1 -= 1
        z2 += 1
    tmp = len(a)
    for i in range(1, round(n/2)+1):
        a.append(a[tmp-i-1])


for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print('')