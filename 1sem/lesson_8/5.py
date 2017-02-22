N = int(input())
f = open('input_5.txt')
s = f.read().split('\n')
lang = []
a = {}
for i in range(N):
    lang.append(input())
for i in lang:
    for j in s:
        if i in j.split(':')[1].split():
            a[j] = i
res = []
for i in a:
    res.append(i.split(' : '))
for i in res:
    print(i[0], ':', i[1])