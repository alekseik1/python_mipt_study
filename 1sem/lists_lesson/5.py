k = input().split()
k, n = int(k[0]), int(k[1])

a = [1]*k

def fib(k, n):
    if k >= n:
        return 1
    else:
        i = 0
        j = 0
        while True:
            a[i] = sum(a)
            i += 1
            j += 1
            if i > len(a)-1:
                i %= len(a)
            if j == n: break
    return a[0]
print(fib(k, n))