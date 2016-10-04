a = [1, 2, 3, 4, 2]
for i in range(1, int(input())+1):
    a.insert(len(a) - a[-1]-1, a[-1])
    del a[-1]
[print(x, end=' ') for x in a]