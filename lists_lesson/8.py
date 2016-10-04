N = int(input())
a = []
for k in range(N): a.extend(map(int, input().split()))
T = int(input())

j = 0
k = 0
for k in range(N):
    if (a[2*k] <= T) and (a[1+2*k] >= T):
        j += 1
print(j)