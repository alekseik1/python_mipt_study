def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if not(left):
        res += right
    else:
        res += left
    return res
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(*merge(A, B))
