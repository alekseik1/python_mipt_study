n = int(input())
l = [int(x) for x in input().split()]
r = 0
M = 10**9
for i in range(n):
    for j in range(i, n):
        if abs(l[j]) == abs(l[i]) and l[i] < 0 and i != j:
            r = j - i
            if 0 < r < M:
                m = r
if M == 10**9:
    print(0)
else:
    print(m)