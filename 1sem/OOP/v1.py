class Vector():
    def __init__(self, s='0,0'):
        self.x = float(s.split(',')[0])
        self.y = float(s.split(',')[1])

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ']'

    def __add__(self, sec):
        assert isinstance(sec, Vector)
        return Vector(str(self.x+sec.x)+','+str(self.y+sec.y))

    def sc_proizv(self, b):
        assert isinstance(b, Vector)
        return self.x*b.x + self.y*b.y

    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

#a = Vector('2,5')
#b = Vector('3,6')
#print(a.sc_proizv(b))
#print(a.sum(b))
#------- 2 task --------
N = int(input())
A = []
for i in range(N):
    A.append(Vector(input()))
B = A[:]
for i in range(N):
    B[i] = abs(B[i])
print(A[B.index(max(B))])