N = int(input())

def check(a, b):
    if (b == 0):
        return a;
    return check(b, a%b);
res = []
for i in range(N):
    a, b = map(int, input().split())
    if check(a, b) == 1:
        res.append([a, b])
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end=' ')
    print('')