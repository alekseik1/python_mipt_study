x = []
y = []
strike = False
for i in range(8):
    s = list(map(int, input().split()))
    x.append(s[0])
    y.append(s[1])

#Horizontal
for i in range(8):
    for j in range(i):
        if x[i] == x[j]:
            strike = True
        if y[i] == y[j]:
            strike = True
        if abs(x[i] - x[j]) == abs(y[i] - y[j]):
            strike = True
if strike:
    print('YES')
else:
    print('NO')