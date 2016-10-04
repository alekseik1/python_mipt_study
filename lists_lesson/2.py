a = []
for i in range(5): a.append(i)

if len(a) %2 != 0: a.append(a[-1]); b = True
a[::2], a[1::2] = a[1::2], a[::2]
if b: del a[-1]

print(a)