a = int(input())
s = []
for i in range(a):
    if i %3 == 1 and i <= a: s.append(i**2)
print(sum(s))