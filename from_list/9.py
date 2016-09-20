import turtle as t
t.shape('turtle')

def draw_circle(r):
  a = 3
  dx= r * 3.14/180*a
  for i in range(1000):
    t.forward(dx)
    r = r + 0.5
    dx= r * 3.14/180*a
    t.left(a)
draw_circle(50)
