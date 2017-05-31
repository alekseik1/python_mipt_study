def lev(s, t):
    if s == t: return 0
    elif len(s) == 0: return len(t)
    elif len(t) == 0: return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    return v1[len(t)]

def lev1(s1, s2):
    m, n = len(s1), len(s2)
    if m == 0:
        return n
    if n == 0:
        return m
    mtx = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        mtx[i][0] = i
    for j in range(1, n + 1):
        mtx[0][j] = j
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                mtx[i][j] = mtx[i - 1][j - 1]
            else:
                mtx[i][j] = min(mtx[i - 1][j] + 1,
                                mtx[i][j - 1] + 1,
                                mtx[i - 1][j - 1] + 1)
    return mtx[m][n]
'''

def distance(a, b):
    n = len(a)
    m = len(b)
    d = [[0]*n for i in range(m)]
    for i in range(m):
        d[i][0] = i
    for i in range(n):
        d[0][i] = i
    for i in range(1, n):
        for j in range(1, m):
            if a[i] == b[j]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1])
    return d
'''
print(lev1(input(), input()))
