a = int(input())
ap = -2
i = 0
ip = 0
rising = False
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

        if a > ap and rising:
            i += 1
        elif a < ap and not rising:
            i += 1
        else:
            ip = max(i, ip)
            i = 1
            if a > ap: rising = True
            elif a < ap: rising = False
            if a == ap: i = 0
else:
    i = i
k = max(i, ip)
print(k+1)
