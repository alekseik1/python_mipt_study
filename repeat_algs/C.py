Fres = [0, 0]
Gres = [0, 0]
def F(n):
    if n <= 2:
        return 0
    if n > 2:
        for i in range(2, n):
            Fres.append(Fres[i-1] + 2*Gres[i-2] + 1)
            Gres.append(Fres[i-2] + 2*Gres[i-1] - 1)
        return Fres[n-1]

N = int(input())
print(F(N))
