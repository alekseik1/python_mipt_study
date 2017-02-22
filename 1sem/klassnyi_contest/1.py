import sys
s = sys.argv
if len(s[1:]) == 0:
  sys.exit(0)
res = 0
for i in s[1:]:
  if i.find('.') != -1:
    pass
  try:
    res += int(i)
  except:
    pass
sys.exit(res)
