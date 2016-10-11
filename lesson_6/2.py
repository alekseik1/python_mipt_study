import random
N = 300000
s = 0
a = -3
b = 3
step = (b-a)/N
for i in range(1, N+1):
    st = random.uniform(a, b)
    if st > 2 or st < -2: continue
    s += -1*(st)**2+4
s *= (b-a)/N
print(s)