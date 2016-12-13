def sync_sort(A, B):
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if A[j] < A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                B[j], B[j + 1] = B[j + 1], B[j]
            if A[j] == A[j+1]:
                B[j], B[j+1] = B[j+1], B[j]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sync_sort(A, B)
print(*B)