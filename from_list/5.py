import turtle as t
t.shape('turtle')

def draw_circle(r):
  a = 3
  dx= r * 3.14/180*a
  for i in range(120):
    t.forward(dx)
    t.left(a)
for i in range(6):
  draw_circle(100)
  t.right(60)

