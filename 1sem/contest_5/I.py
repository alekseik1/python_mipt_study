x = []
y = []
N = int(input())
ro = int.max
strike = False
for i in range(N):
    s = list(map(int, input().split()))
    x.append(s[0])
    y.append(s[1])

for i in range(N):
    for j in range(i):
        print('eap')
