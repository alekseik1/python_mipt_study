import sys
k = 0
for arg in sys.argv:
    if len(arg)%3 == 0:
        k += 1
print(k)