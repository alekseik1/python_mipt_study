import math
import threading
#N = int(input('Number of CPUs'))
a = int(input())
def check(a):
    if(a == 2): return True
    b = True
    for i in range(2, int(math.sqrt(a))+2):
        if a%i == 0:
            b = False
    if b: return True
    else: return False
#e1 = threading.Event()
#t1 = threading.Thread(target=check, args=a)
#t1.start()
#e1.set()
#t1.join()
#print(razl(a))
#if check(a): print("YES")
#else: print("NO")

def razl(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

print(razl(a))