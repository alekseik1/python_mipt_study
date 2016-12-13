def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    return 0 if get_next.seed == 0 else (get_next.seed**2%100000 + 1)

get_next.seed = int(input())
x = get_next()
a = dict()
i = 0
while x != 0:
    if x in a:
        a[x].append(i)
    else:
        a[x] = [i]
    i += 1
    x = get_next()

keys = sorted(a, reverse=True)
answer = []
for i in keys:
    if i == keys[0]:
        answer += a[i]
    else:
        break
print(*answer)
