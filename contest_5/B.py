a = input().split()
b = []
for i in a:
    k = i[0].upper() + i[1:].lower()
    b.append(k)
print(*b)