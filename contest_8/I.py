N=int(input())
A=[]
for i in range(N):
    A.append(list(map(float,input().strip().split())))
A.sort(key= lambda g:g[0],reverse=True)
A.sort(key= lambda g:g[1])
for i in range(N):
    B=[str("%.2f" % A[i][0]),str("%.3f" % A[i][1])]
    print(' '.join(B))