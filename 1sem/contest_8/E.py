a = input()
k = 0
for ch in a:
    if ch == '(': k += 1
    elif ch == ')':
        k -= 1
        if k < 0: break
if k == 0:
    print('YES')
else:
    print('NO')