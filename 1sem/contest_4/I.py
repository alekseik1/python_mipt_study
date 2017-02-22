a = int(input())
if a!=0 : b = int(input())
if a !=0 :
    if b !=0 : c = int(input())
i = 0
while (a!=0) and (b!=0) and (c!=0):
    if (b>a) and (b>c): i += 1
    a,b = b,c
    c = int(input())
print(i)
