import random
N = 10000
s = 0
a = -2
b = 2
step = (b-a)/N
for i in range(1, N+1):
    st = random.uniform(-2, 2)
    s += -1*(st)**2+4
s *= (b-a)/N
print(s)