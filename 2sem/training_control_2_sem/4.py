n = int(input())
m = [int(x) for x in input().split()]
print(*sorted([x for x in m if x % 2 == 0]), *sorted([x for x in m if x % 2 == 1]))
