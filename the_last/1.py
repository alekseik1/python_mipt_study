def check_and_do_properly(A):
  c = ord('A')
  for i in range(len(A)):
    if A[i] >= 10:
      A[i] = chr(A[i] - 10 + c)
  return A

def perevod(chislo, base):
  A = []
  while chislo > 0:
    A.append(chislo % base)
    chislo = chislo // base
  A = A[::-1]
  A = check_and_do_properly(A)
  s = ''
  for i in A:
    s += str(i)
  return s

print(len(perevod(int(input()), 36)))
