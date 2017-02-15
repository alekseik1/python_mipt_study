Fres = [0, 0]
Gres = [0, 0]
def F(n):
    if n <= 2:
        return 0
    if n > 2:
        Fres.append(Fres[n-1] + 2*Gres[n-2] + 1)

def G(n):
    if n <= 2:
        return 0
    if n > 2:
        Gres.append(Fres[n-2] + 2*Gres[n-1] - 1)
N = int(input())
print(F(N))