s = list(map(int, input().split()))
A = [[0]*(s[1]+1) for i in range((s[0]+1))]

def dinamika(n, k):
    if A[n][k] != 0:
        return A[n][k]
    if n == 0:
        A[n][k] = 1
        return 1
    elif k == 0:
        A[n][k] = 1
        return 1
    else:
        A[n][k] = dinamika(n-1, k) + dinamika(n, k-1)
        return A[n][k]

print(dinamika(s[0], s[1]))
