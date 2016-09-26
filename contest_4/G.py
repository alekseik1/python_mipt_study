a = int(input())
ap = -2
i = 0
ip = 0
if a != 0:
    while True:
        s = input()
        if s == "":
            continue
        else:
            s = int(s)
        if s == 0:
            break
        ap = a
        a = s

        if ap == a:
            i += 1

        if ap != a and i != 0:
            ip = i
            i = 0
else:
    i = ip = 0
k = max(i, ip)
print(k+1)
