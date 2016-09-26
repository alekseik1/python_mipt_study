a = int(input())
if a!=0 : b = int(input())
if a !=0 :
    if b !=0 : c = int(input())
loc = 0
kmin = 10**15
k = 10**15 + 1
while (a!=0) and (b!=0) and (c!=0):
    if (b>a) and (b>c):
        loc += 1
        if k<kmin : kmin = k
        k = 0
    elif loc>0 : k +=1
    a,b = b,c
    c = int(input())
if (loc<2) : print('0')
else : print(kmin+1)

