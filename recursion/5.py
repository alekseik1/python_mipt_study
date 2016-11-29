import turtle
turtle.speed(50)
def do_magic(l,n):
    if n == 0:
        turtle.forward(l)
        return

    turtle.left(45)
    do_magic((l/2)*(2**0.5), n-1)
    turtle.right(90)
    do_magic((l/2) * (2 ** 0.5), n-1)
    turtle.left(45)
do_magic(300, 7)
