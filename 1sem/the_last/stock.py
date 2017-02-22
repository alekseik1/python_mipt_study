n = int(input())
max_cost = 3601
payment = [[max_cost]*3 for i in range(3)]
for i in range(n):
    payment.append(list(map(int, input().split())))
x = [0, 0, 0]
for i in range(3, n+3):
    a = [x[i-1]+payment[i][0]]+[x[i-2]+payment[i-1][1]]+[x[i-3]+payment[i-2][2]]
    x.append(min(a))
print(x[n+2])
