x = y = 0
while True:
    a = input()
    if a == "Treasure!": break
    a = a.split()
    if(a[0] == "North"):
        y += int(a[1])
    elif(a[0] == "South"):
        y -= int(a[1])
    elif(a[0] == "West"):
        x -= int(a[1])
    elif(a[0] == "East"):
        x += int(a[1])
print(x, y)