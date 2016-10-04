N = int(input())
a = list(map(int, input().split()))
for i in range(N):
    more = 0
    less = 0
    for j in range(N):
        if a[i] < a[j]:
            more += 1
        elif a[i] > a[j]:
            less += 1
    if (more == N // 2) and (less == N // 2):
        print(a[i])