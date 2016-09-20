import turtle as t
t.shape('turtle')
s = 5
a = 90
n = int(input())
for i in range(4*n):
  t.forward(s)
  t.right(a)
  s+=5
