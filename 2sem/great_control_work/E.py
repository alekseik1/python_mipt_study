n = int(input())
A = [int(x) for x in input().split()]
ro = 0
MM = 10**9
for i in range(n):
    for j in range(i, n):
        if abs(A[j]) == abs(A[i]) and A[i] < 0 and i != j:
            ro = j - i
            if ro < MM and ro > 0:
                MM = ro
if MM == 10**9:
    print(0)
else:
    print(MM)