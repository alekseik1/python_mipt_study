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
m = 999999999
r = []
for key in s:
    if s[key]<m:
        m = s[key]
        r = [key]
    elif s[key] == m:
        r.append(key)
r = sorted(r)
print(*r)