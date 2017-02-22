def Rotate(A):
    return rev_costil(Transpose(A))
def Transpose(A):
    n = len(A)
    m = len(A[0])
    ret = []
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp.append(A[i][j])
        ret.append(tmp)
    return ret
def rev_costil(A):
    ret = []
    for i in range(len(A)):
        ret.append(A[i][::-1])
    return ret
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a = Rotate(a)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print('')


