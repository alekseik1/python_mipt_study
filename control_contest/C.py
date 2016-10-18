n = int(input())
s2 = input().split()
max = -2500000
min = 2500000
nmin = 0
nmax = 0
nom = -1
s1 = []

for i in range (n):
    nom +=1
    a = int(s2[nom])
    s1.append(a)
    if (a % 2 == 0) and (a < min):
        min = a
        nmin = nom
    if (a > max) and ((a % 2 == 1) or (a % 2 ==-1)):
        max = a
        nmax = nom

if (min == 2500000) or (max == -2500000):
    print(*s1)

else:
    s1[nmax],s1[nmin]=s1[nmin],s1[nmax]
    print(*s1)