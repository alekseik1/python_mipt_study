# Сортировка пузырьком.
# O(n^2)
def buble_sort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if A[j] < A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                
# Тесты
A = list(map(int, input().split()))
buble_sort(A)
print(*A)
