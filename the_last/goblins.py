def sort(A):
    B = [0]*len(A)
    for i in range(1, len(A)):
        for j in range(1, len(A) - i):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
                B[j] += 1
    res = []
    for i in range(len(A)):
        res.append(str(A[i])+':'+str(B[i]))
    return res
a = list(map(int, input().split()))
print(*sort(a))
