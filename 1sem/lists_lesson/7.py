a = list(map(int, input().split()))
n = len(a)
for i in range(n-1):
    if (a[i] == 2):
        if a[i+1] != 2:
            a[i] = 0
            n -= 1
print(sum(a)//n)