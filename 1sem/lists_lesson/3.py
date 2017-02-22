a = list(map(int, input().split()))
def one():
    for i in range(len(a)//2):
        print(a[i], a[-(i+1)], end=' ')
    if len(a)%2 == 1: print(a[len(a)//2])
one()