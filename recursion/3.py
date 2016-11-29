import turtle

turtle.speed(20)


def move_sneg(l, n):
    if n == 0:
        turtle.forward(l)
        return

    for i in range(n):
        move_sneg(l / 3, n - 1)
        turtle.left(60)
        move_sneg(l / 3, n - 1)
        turtle.right(120)
        move_sneg(l / 3, n - 1)
        turtle.left(60)
        move_sneg(l / 3, n - 1)
        turtle.right(60)
        return


def koch(l, n):
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

def move(l, n):

    koch(l, n)
    turtle.right(120)
    koch(l, n)
    turtle.right(120)
    koch(l, n)
    turtle.right(120)
    return

move(100, 3)

#move_sneg(1000, 10)
