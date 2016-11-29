import turtle
turtle.speed(20)
def koch(l, n):
    assert n >= 0
    assert l >= 0
    #turtle.shape('turtle')
    if n == 0:
        turtle.forward(l)
        return

    for i in range(n):
        koch(l/3, n-1)
        turtle.left(60)
        koch(l/3, n-1)
        turtle.right(120)
        koch(l/3, n-1)
        turtle.left(60)
        koch(l/3, n-1)
        return

l = 2000
n = int(input())
koch(l, n)