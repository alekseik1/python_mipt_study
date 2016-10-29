a, b = input().split()
a, b = '0x' + a, '0x' + b
res = hex(int(a, 16) ^ int(b, 16))
print(res[2:])