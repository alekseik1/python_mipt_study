import turtle as t
t.shape('turtle')
a = int(input())
b = int(input())
s = 50
def draw_circle(r, a):
  dx= r * 3.14/180*a
  for i in range(360//a):
    t.forward(dx)
    t.left(a)

def reg_pol(n, r):
  draw_circle(r, 360//n)
reg_pol(a, s)
t.penup()
t.goto(2*s, s/2)
t.pendown()

t.forward(s)
t.backward(s/2)
t.left(90)
t.forward(s/2)
t.backward(s)

t.penup()
t.forward(s)
t.left(90)
t.backward(s*2.5)
t.pendown()

reg_pol(b, s)

t.penup()
t.goto(5.5*s+5, s/2)
t.pendown()
t.forward(20)
t.right(90)
t.penup()
t.forward(10)
t.pendown()
t.right(90)
t.forward(20)

t.penup()
t.forward(2*s)

t.pendown()
reg_pol(a+b, s)
