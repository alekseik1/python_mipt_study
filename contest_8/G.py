a = input()
a = a[:a.index('.')]
c = []
for i in a:
    c.append(ord(i))
c.sort()
for i in c:
    print(chr(i), end='')
if a != '':
    print('.')