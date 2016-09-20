def fac(n):
  if n == 0:
    return 1
  else:
    return n*fac(n-1)
n = 100
while True:
  if fac(n) > 0:
    print(n+1+2)
    n+=1
