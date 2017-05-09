n, m = [int(x) for x in input().split()]
s = {x:set() for x in range(1, n+1)}
for i in range(1, m+1):
    a, b = [int(x) for x in input().split()]
    s[a].add(b)
    s[b].add(a)
all = [x for x in range(n)]
left = []
right = []
right.append(all.pop())   # Начнем
chelovek = all.pop()
ex = False
while all:
    ex = True
    f = -1
    for i in s[chelovek]:
        if i in left:   # Если недруг слева - то пометим, чтоб этого человека отправили вправо
            f = 1
        if f == 1 and i in right:      # Если уже пометили, чтоб отправили вправо, но и там оказался недруг, то плохи дела
            f = -2
            break
    if f == -1:
        left.append(chelovek)
    elif f == 1:
        right.append(chelovek)
    chelovek = all.pop()
if not ex:
    print('YES')
    print(chelovek)
    exit(0)
if f == -2:
    print('NO')
else:
    print('YES')
    print(*left)
