n = int(input())
s = [int(x) for x in input().split()]
k = 0
su = 0
for i in range(len(s)):
    if s[i] != 5:
        su += s[i]//5 - 1
    else:
        su -= 1
    k = max(k, su)
if k < 0:
    print(0)
else:
    print(k)