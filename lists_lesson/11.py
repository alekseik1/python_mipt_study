a = int(input())
s = []
for i in range(1, round(a**0.5)+1):
    if i**2%3==1: s.append(i**2)
print(sum(s))