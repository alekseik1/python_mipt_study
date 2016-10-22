n = int(input())
#n = 5
a = []
for i in range(n):
    tmp = []
    for j in range(n):
        if i == j or n %2 == 1 and i == (n-1)/2 or n %2==1 and j == (n-1)/2 or i+j == n-1:
            tmp.append('*')
        else:
            tmp.append('.')
    a.append(tmp)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print('')