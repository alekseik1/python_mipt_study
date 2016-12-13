def sort_with_change(A, B):
    for k in range(1, len(A)):
        for i in range(0, len(A)-k):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                B[i], B[i+1] = B[i+1], B[i]
                B[i] += 1
                B[i+1] += 1
def sort_with_change_without_counting(A, B):
    for k in range(1, len(A)):
        for i in range(0, len(A)-k):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                B[i], B[i+1] = B[i+1], B[i]

A = [int(x) for x in input().split()]
B = [0]*len(A)
sort_with_change(A, B)
dic = {}
for i in range(len(B)):
    if A[i] not in dic:
        dic[A[i]] = B[i]
    else:
        dic[A[i]] += B[i]
keys = list(dic.keys())
values = list(dic.values())
sort_with_change_without_counting(keys, values)
result = []
for i in range(len(keys)):
    result.append(str(keys[i]) + ':' + str(values[i]))
print(*result)
