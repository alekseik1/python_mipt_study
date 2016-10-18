x1, y1, z1, Vx1, Vy1, Vz1 = map(int, input().split())
x2, y2, z2, Vx2, Vy2, Vz2 = map(int, input().split())
x3, y3, z3, Vx3, Vy3, Vz3 = map(int, input().split())

def div(x, y, caseZero=1):
    if x == y == 0:
        return caseZero
    elif (x == 0 and y != 0) or (y == 0 and x != 0):
        return caseZero+1
    else:
        return x/y

# Коллинеарность
t = div(Vx1, Vx2)
if div(Vx1, Vx2, t)/t == div(Vy1, Vy2, t)/t == div(Vz1, Vz2, t)/t:
    # Совпадают
    if x1 == x2 and y1 == y2 and z1 == z2:
        print(-1)
        exit(0)
    else:
        print(0)
        exit(0)
t = div(Vx1, Vx3)
if div(Vx1, Vx3, t)/t == div(Vy1, Vy3, t)/t == div(Vz1, Vz3, t)/t:
    if x1 == x3 and y1 == y3 and z1 == z3:
        print(-1)
    else:
        print(0)
    exit(0)
t = div(Vx2, Vx3)
if div(Vx2, Vx3, t)/t == div(Vy2, Vy3, t)/t == div(Vz2, Vz3, t)/t:
    if x2 == x3 and y2 == y3 and z2 == z3:
        print(-1)
    else:
        print(0)
    exit(0)

# Все векторы попарно неколлинеарны

t = div((x1 - x2), (Vx2 - Vx1))
tx1 = div((x1 - x2), (Vx2 - Vx1), t)/t
ty1 = div((y1 - y2), (Vy2 - Vy1), t)/t
tz1 = div((z1 - z2), (Vz2 - Vz1), t)/t

tx2 = div((x1 - x3), (Vx3 - Vx1), t)/t
ty2 = div((y1 - y3), (Vy3 - Vy1), t)/t
tz2 = div((z1 - z3), (Vz3 - Vz1), t)/t

tx3 = div((x2 - x3), (Vx3 - Vx2), t)/t
ty3 = div((y2 - y3), (Vy3 - Vy2), t)/t
tz3 = div((z2 - z3), (Vz3 - Vz2), t)/t

if tx1 == tx2 == tx3 and ty1 == ty2 == ty3 and tz1 == tz2 == tz3:
    print(1)
else:
    print(0)
exit(0)
