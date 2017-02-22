import random
def qsort(A):
    if len(A) <= 1:
        return A
    mid_ss = A[0]
    left = []
    right = []
    mid_solo = []
    for i in A:
        if i > mid_ss:
            right.append(i)
        elif i < mid_ss:
            left.append(i)
        else:
            mid_solo.append(i)
    return qsort(left)+mid_solo+qsort(right)

for i in range(20):
    A = [random.randint(1, 1000) for x in range(1000)]
    print(qsort(A) == sorted(A))