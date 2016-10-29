a = input()
k = 0
tmp = []
if a.count('(') != a.count(')'):
    print('NO')
else:
    for i in a:
        if i == '(':
            tmp.append(1)
        else:
            tmp.append(-1)