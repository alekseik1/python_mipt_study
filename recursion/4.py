import turtle
turtle.speed(150)

def draw(l,n):
    if n == 0:
        turtle.forward(l)
        return
    
    draw(l/4, n-1)
    turtle.left(90)
    draw(l/4, n-1)
    turtle.right(90)
    draw(l/4, n-1)
    turtle.right(90)
    draw(l/4, n-1)
    draw(l/4, n-1)
    turtle.left(90)
    draw(l/4, n-1)
    turtle.left(90)
    draw(l/4, n-1)
    turtle.right(90)
    draw(l/4, n-1)
draw(500, 3)