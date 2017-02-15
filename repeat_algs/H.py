N = int(input())
A = [int(x) for x in input().split()]
sum1 = sum(A[:])
A.sort()
s = 0
for i in range(N//2):
    s += A[i]
print(sum1 - s)
