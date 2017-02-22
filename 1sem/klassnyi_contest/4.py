m = ['c', 's', 'h', 'd']
d = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
sort_rules = []
for i in d:
    for j in m:
        sort_rules.append(i+j)

n = int(input())
s = input()
A = {}
assert len(s)%2 == 0
for i in range(0, len(s), 2):
    stroka = s[i]+s[i+1]
    A.update({sort_rules.index(stroka): stroka})
l = sorted(list(A.keys()))
for i in l:
    print(A[i], end='')