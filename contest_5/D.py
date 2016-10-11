a = input().split('.')
if len(a) == 4:
  b = True
  for i in a:
    try:
        if 0 <= int(i) < 256:
            continue
        else:
            b = False
            break
    except:
        b = False
  if b:
    print('YES')
  else:
    print('NO')
else:
  print('NO')