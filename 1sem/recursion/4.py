import turtle
turtle.speed(150)

def cherepaha(l,n):
    if n == 0:
        turtle.forward(l)
        return
    
    cherepaha(l/4, n-1)
    turtle.left(90)
    cherepaha(l/4, n-1)
    turtle.right(90)
    cherepaha(l/4, n-1)
    turtle.right(90)
    cherepaha(l/4, n-1)
    cherepaha(l/4, n-1)
    turtle.left(90)
    cherepaha(l/4, n-1)
    turtle.left(90)
    cherepaha(l/4, n-1)
    turtle.right(90)
    cherepaha(l/4, n-1)
cherepaha(500, 3)
