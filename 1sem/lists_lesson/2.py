a = [1, 1, 3, 4, 5, 6]
#for i in range(1, 6): a.append(i)

def one(b):
    if b == 1: a.append(a[-1])
    a[::2], a[1::2] = a[1::2], a[::2]
    if b == 1: del a[-1]
    return a

def two():
    a[1::], a[0]= a[:-1:], a[-1]
    return a

def three():
    for i in range(min(a), max(a)+1):
        if a.count(i) - 1 == 0: print(i, end= ' ')
    print('\n')

def four():
    print(max(map(a.count, a)))

print(one(len(a)%2))
print(two())
three()
four()