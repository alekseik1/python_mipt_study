def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2 + 3*get_next.seed)%999 + 1

get_next.seed = int(input())
x = get_next()
s = {}
while x != 0:
    if x not in s:
        s[x] = 1
    else:
        s[x] += 1
    x = get_next()
maks = 999999999
res = []
for i in s:
    if s[i] < maks:
        maks = s[i]
        res = [i]
    elif s[i] == maks:
        res.append(i)
res = sorted(res)
print(*res)