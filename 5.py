import turtle
turtle.shape('turtle')
s = 50
a = 90
p = 30
for i in range(900):
  for i in range(4):
    turtle.forward(s)
    turtle.left(a)
  turtle.penup()
  turtle.backward(p/2)
  turtle.right(a)
  turtle.forward(p/2)
  turtle.left(90)
  s+=p
  turtle.pendown()
