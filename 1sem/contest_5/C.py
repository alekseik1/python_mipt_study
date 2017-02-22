a = input().split()
s = ""
if a[1] == "a.m.":
    a = a[0].split(':')
    if int(a[0]) < 10:
        s += "0" + a[0]
    else:
        s += a[0]
    s += ":"
    if len(a[1]) > 1:
        s += a[1]
    else:
        s += "0" + a[1]
elif a[1] == "p.m.":
    a = a[0].split(':')
    if int(a[0]) == 12:
        s += a[0] + ":"
    else:
        s += str(int(a[0])+12) + ":"
    if len(a[1]) > 1:
        s += a[1]
    else:
        s += "0" + a[1]
print(s)