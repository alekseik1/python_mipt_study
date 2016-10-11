N = int(input())
a = list(map(int, input().split()))
i0, j0 = 0, 0
d = max(a)-min(a)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if abs(a[i]-a[j]) <= d:
            d = abs(a[i] - a[j])
            i0, j0 = i, j
print(i0, j0)