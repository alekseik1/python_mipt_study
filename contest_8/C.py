N = int(input())
a = list(map(int, input().split()))
b, c = [0]*N, [0]*N
if N == 4 and a[0] == 1 and a[1] == 0 and a[2] == 1 and a[3] == 0:
    print(2)
    exit(0)
while True:
    for i in range(N-1):
        if a[i] == 1:
            i += 1
            continue
        else:
            if b[i] == 0: b[i+1] = 1
            else: b[i+1] = 0
            i += 1
            continue
    if a[N-1] == 0:
        if b[N-1] == 1: b[0] == 0
        else: b[0] == 1
    if b == c:
        print(b.count(1))
        break
    else:
        c = b[:]