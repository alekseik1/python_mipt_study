import turtle
turtle.speed(50)
def do_motion(n, b):
    if n == 0:
        return b
    res = []
    k = 0
    j = 0

    for i in range(len(b)*2+1):
        if i % 2 == 0:
            if k == 0:
                res.append(k)
                k = 1
            else:
                res.append(k)
                k = 0
        else:
            res.append(b[j])
            j += 1
    return do_motion(n-1, res)
def draw(l, n):
    x = l / n
    A=[]
    act = do_motion(n,A)
    turtle.forward(x)
    for i in range(len(act)):
        if act[i] == 0:
            turtle.right(90)
        else:
            turtle.left(90)
        turtle.forward(x)
draw(20, 20)