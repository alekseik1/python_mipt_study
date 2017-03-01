n, m = [int(x) for x in input().split()]
x0, y0 = [int(x) for x in input().split()]
x1, y1 = [int(x) for x in input().split()]
res = [[True]*m for x in range(n)]
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == 'X':
            res[i][j] = False
q_x = [x0]
q_y = [y0]
res[x0][y0] = 0
not_found = False
while True:
    tmp_x = q_x.pop(0)
    tmp_y = q_y.pop(0)

    if type(res[tmp_x+1][tmp_y]) == bool and res[tmp_x+1][tmp_y]:
        res[tmp_x+1][tmp_y] = res[tmp_x][tmp_y] + 1
        q_x.append(tmp_x+1)
        q_y.append(tmp_y)
    elif not (type(res[tmp_x+1][tmp_y]) == bool):
        res[tmp_x+1][tmp_y] = min(res[tmp_x][tmp_y] + 1, res[tmp_x+1][tmp_y])

    if type(res[tmp_x-1][tmp_y]) == bool and res[tmp_x-1][tmp_y]:
        res[tmp_x-1][tmp_y] = res[tmp_x][tmp_y] + 1
        q_x.append(tmp_x-1)
        q_y.append(tmp_y)
    elif not (type(res[tmp_x-1][tmp_y]) == bool):
        res[tmp_x-1][tmp_y] = min(res[tmp_x][tmp_y] + 1, res[tmp_x-1][tmp_y])

    if type(res[tmp_x][tmp_y+1]) == bool and res[tmp_x][tmp_y+1]:
        res[tmp_x][tmp_y+1] = res[tmp_x][tmp_y] + 1
        q_x.append(tmp_x)
        q_y.append(tmp_y+1)
    elif not (type(res[tmp_x][tmp_y+1]) == bool):
        res[tmp_x][tmp_y+1] = min(res[tmp_x][tmp_y] + 1, res[tmp_x][tmp_y+1])

    if type(res[tmp_x][tmp_y-1]) == bool and res[tmp_x][tmp_y-1]:
        res[tmp_x][tmp_y-1] = res[tmp_x][tmp_y] + 1
        q_x.append(tmp_x)
        q_y.append(tmp_y-1)
    elif not (type(res[tmp_x][tmp_y-1]) == bool):
        res[tmp_x][tmp_y-1] = min(res[tmp_x][tmp_y] + 1, res[tmp_x][tmp_y-1])

    if len(q_x) == 0:
        if type(res[x1][y1]) == bool:
            not_found = True
        break
if not not_found:
    print(res[x1][y1])
else:
    print('INF')
