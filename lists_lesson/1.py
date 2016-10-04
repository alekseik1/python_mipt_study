def one():
    for i in input().split()[::2]: print(i, end=' ')

def two():
    a = input().split()
    print(max(a), a.index(max(a)))

def three():
    [print(x, end=' ') for x in input().split()[::-1]]
three()