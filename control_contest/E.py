a, b = map(float, input().split())
if b > (1+a**2) or b < (-2-a**2):
    print("YES")
else:
    print("NO")