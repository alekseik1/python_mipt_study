class Vector():
    def __init__(self, s='0,0'):
        self.x = float(s.split(',')[0])
        self.y = float(s.split(',')[1])

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ']'

    def __sub__(self, b):
        return Vector(str(self.x - b.x) + ',' + str(self.y - b.y))
    def __mul__(self, b):
        return Vector(str(self.x * b) + ',' + str(self.y * b))

    def __add__(self, sec):
        assert isinstance(sec, Vector)
        return Vector(str(self.x+sec.x)+','+str(self.y+sec.y))

    def sc_proizv(self, b):
        assert isinstance(b, Vector)
        return self.x*b.x + self.y*b.y

    def distance(self):
        return abs(self)

    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def per(self, a, b):
        return (self-a).distance() + (self-b).distance() + (a - b).distance()

    def plus(self, a, b):
        return ((self.x - b.x) * (a.y - b.y) - (a.x - b.x) * (self.y - b.y)) / 2

N = int(input())
A = []
for i in range(N):
    A.append(Vector(input()))

maxP = 0
maxS = 0

for i in A:
    for j in A:
        for k in A:
            if i.per(j, k) > maxP:
                maxP = i.per(j, k)
            if i.plus(j, k) > maxS:
                maxS = i.plus(j, k)

print ('Max P=', max)
print ('Max S=', maxS)
