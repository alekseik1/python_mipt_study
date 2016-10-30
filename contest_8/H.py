N = int(input())
l = input().split()
ml = 0
l1 = []
for i in l:
    if len(i) > ml: ml = len(i)
for i in l:
    l1.append('0'*(ml-len(i)) + i)
for i in range(len(l1)):
    l1[i] = l1[i][::-1]
l = l1
l = list(map(int, l))
l.sort()
for i in range(len(l)):
    l[i] = str(l[i])
    l[i] = l[i][::-1]
for i in range(len(l)):
    j = 0
    while True:
        if int(l[i][j]) != 0: break
        j += 1
    l[i] = l[i][j::]
print(*l)
