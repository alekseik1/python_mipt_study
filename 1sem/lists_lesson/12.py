f = open('input.txt', 'r')
a = list(map(int, f.read().split('\n')))
f.close()
w = h = 0
h_max = 0
S = 0
res = 0
for i in range(len(a)):
    if(a[i] == 0):
        S = (w*h)
        if S > res:
            res = S
            h_max = h
        w = 0
        h = 0
        continue
    w += 1
    if(a[i] >= h):
        h0 = h
        S = w*h
        h = a[i]
        if h > res:
            res = h
            h_max = h
    else:
        h0 = h
        h = a[i]
        if(w*h > S):
            S = w*h
            h_max = h
            res = S
f = open('output.txt', 'w')
print(S, file=f)
print(h_max, file=f)
f.close()
