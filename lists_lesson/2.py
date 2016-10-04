a = [1, 2, 2, 3, 3, 3]
#for i in range(1, 6): a.append(i)

def one():
    if len(a) %2 != 0: a.append(a[-1]); b = True
    a[::2], a[1::2] = a[1::2], a[::2]
    if b: del a[-1]

def two():
    a[1::], a[0]= a[:-1:], a[-1]
    return a

def three():
    for i in range(min(a), max(a)):
        if a.count(i) - 1 == 0: print(i)
three()