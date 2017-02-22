def do_sort(g,i):
    if(len(g)-(i+1)<0):
        return '0'
    else:
        return g[len(g)-(i+1)]
def sort_magic(Makl,n):
    for i in range(n):
        Makl.sort(key=lambda g: do_sort(g, n-1-i))
    return Makl
k=int(input())
A=list(map(str,input().strip().split()))
A=sort_magic(A,6)
print(' '.join(A))
