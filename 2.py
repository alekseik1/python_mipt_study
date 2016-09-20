a = int(input())
s1 = "Fizz"
s2 = "Buzz"
s = ''
for i in range(1, a):
  if i%3==0:
    s+= s1
  if i%5==0:
    s+=s2
  if len(s)==0:
    s+=str(i)
  print(s)
  s = ''
