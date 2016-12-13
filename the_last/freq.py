def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2 + 3*get_next.seed)%999 + 1

get_next.seed = int(input())
x = get_next()
a = dict()
while x != 0:
    if x in a:
        a[x] += 1
    else:
        a[x] = 0
    x = get_next()

keys = sorted(a, key=a.get, reverse=True)
MAX = a[keys[0]]
answer = list()
for i in keys:
    if a[i] == MAX:
        answer.append(i)
    else:
        break
answer.sort()
print(*answer)