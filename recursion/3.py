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

def move(l, n):
    if n == 0:
        turtle.forward(l)
        return

    for i in range(n):
        move(l/3, n-1)
        turtle.left(60)
        move(l/3, n-1)
        turtle.right(120)
        move(l/3, n-1)
        turtle.left(60)
        move(l/3, n-1)
        return


move(1000, 5)

#move_sneg(1000, 10)
