def gen():
    n = range(4)
    for i in n:
        yield i*i
a = gen()
for i in a:
    print(i)