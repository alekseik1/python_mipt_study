import turtle
turtle.shape('turtle')
s=100
a=90
for i in range(5):
  turtle.forward(100)
  turtle.left(a)
turtle.right(a)
for i in range(s//2):
  turtle.forward(s/33)
  turtle.left(360/100)
