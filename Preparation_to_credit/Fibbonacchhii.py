def Fib_circle(n):
    A = []
    A.append(1)
    A.append(1)
    i = 2
    while i <= n-1:
        A.append(A[i-1]+A[i-2])
        i += 1
    return A[-1]


def Fib(n):
    A = []
    if n == 1 or n == 2:
        return 1
    else:
        A.append(Fib(n-1) + Fib(n-2))
        return A[-1]
print(Fib_circle(int(input())))