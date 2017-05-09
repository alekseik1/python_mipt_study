n = int(input())
s = input().split()
i = 0
while True:
    tmp = s + s[:i][::-1]
    if tmp == tmp[::-1]:
        break
    i += 1
print(i)
if i != 0:
    print(*s[:i:][::-1])
