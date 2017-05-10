m = [int(x) for x in input().split()]
a = [x for x in m if x % 2 == 0]
b = [x for x in m if x % 2 == 1]
print(*sorted(a), end=' ')
print(*sorted(b))
