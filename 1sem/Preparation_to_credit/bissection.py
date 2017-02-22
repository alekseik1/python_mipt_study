a, b, c = [int(x) for x in input().split()]
def f(x):
    return a*x**2 + b*x + c

def bissection(e):
    minimum = -1
    maximum = 1
    while (f(minimum)) * (f(maximum)) >= 0:
        if f(minimum) == 0:
            return minimum
        if f(maximum) == 0:
            return maximum
        maximum *= 2
        minimum *= 2
    while abs(maximum - minimum) >= e:
        if f(minimum/2) * f(maximum) < 0:
            minimum /= 2
        if f(maximum/2) * f(minimum) < 0:
            maximum /= 2
    print(minimum + '-' + maximum)
print(bissection(0.05))
