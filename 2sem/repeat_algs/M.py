n, m = list(map(int, input().split()))
A = [int(x) for x in input().split()]
#A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(n*m):
    if i%m == 0 and i != 0:
        print('')
    print(A[i], end=' ')