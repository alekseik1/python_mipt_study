prev = int(input())
if prev != 0:
    a = int(input())
    i = 0
    while True:
        if a == 0: break
        if a > prev:
            i += 1
        prev, a = (a, int(input()))
else:
    i = 0
print(i)