def magic(n, k):
    if n == 0:
        return 1
    if k == 0:
        return 0
    if k > n:
        return magic(n, n)
    else:
        return magic(n, k-1) + magic(n-k, k)

global d
d = [[-1]*100]*100

def dec(n, k):
    if n >= 0 and k >= 0 and d[n][k] > 0:
       return d[n][k]
    if n < 0:
        return 0
    if k == 1 or n <= 1:
        return 1
    #if n <= 1 or k == 1: return 1
    d[n][k] = dec(n, k-1) + dec(n-k, k)
    return d[n][k]

N = int(input())
print(dec(N, N))
