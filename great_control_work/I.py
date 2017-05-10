s = input()
l = []
n = len(s)
for i in range(n):
    j = 0
    while j+i < n and i-j >= 0 and s[i-j:i+j+1] == s[i-j:i+j+1][::-1]:
        j += 1
    l.append(2*j - 1)
print(*l)
