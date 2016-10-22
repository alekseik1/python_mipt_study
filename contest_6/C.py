n, m = list(map(int, input().split()))
A = []
#A = [0,3,2,4,2,3,5,5,5,1,2,3]
for i in range(n):
  A.extend(list(map(int, input().split())))
print(A.index(max(A))//m, A.index(max(A))//n)