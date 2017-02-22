import turtle as t
t.shape('turtle')
t.left(90)
s = 50
curr = 90

def set_angle(a, curr):
  while curr != a:
    t.left(90)
    curr = curr+90
    if(curr > 360):
      curr = curr%360
  return curr

while True:
  a = input()
  if a == 'l':
    curr = set_angle(180, curr)
    t.forward(s)
  elif a == 'r':
    curr = set_angle(360, curr)
    t.forward(s)
  elif a == 'd':
    curr =set_angle(270, curr)
    t.forward(s)
  elif a == 'u':
    curr = set_angle(90, curr)
    t.forward(s)
  elif a == '+':
    t.pendown()
  elif a == '-':
    t.penup()
  elif a == 'q':
    print('\nЯ тоже устал, пока!')
    break;
  elif a == 'c':
    t.circle(s)
