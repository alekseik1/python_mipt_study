
def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n+1)
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1, n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]
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
print(distance(input(), input())[-1][-1])
