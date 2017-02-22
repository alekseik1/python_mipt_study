D = int(input())
def fib(n):
    if n == 1 or n == 2:
        return 1
    else: n -= 2
    a, b = 1, 1
    i = 0
    while i != n:
        a, b = a+b, a
        i += 1
    return a
i = 1
s = 0
while True:
    s += fib(i)
    if s >= D:
        break
    i += 1
print(i)