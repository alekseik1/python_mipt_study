t = 0
A =[]
count = 0

def pos(A, t):
    B = []
    for i in range(3):
        B.append([0, 0, 0])
    for xCoor in range(3):
        for yCoor in range(3):
            B[xCoor][yCoor] = A[xCoor][yCoor] + t*A[xCoor][yCoor+3]
    return B

for i in range(3):
    A.append(list(map(int, input().split())))


def is_on_the_same_line(A):
    if (A[0][0] - A[2][0])*(A[1][1] - A[2][1]) == (A[1][0]- A[2][0])*(A[0][1] - A[2][1]):
        if (A[1][2] - A[2][2])*(A[0][0] - A[2][0]) == (A[1][0]- A[2][0])*(A[0][2] - A[2][2]):
            return True
    return False

for t in range(10000):
    if is_on_the_same_line(pos(A, t)):
        count+=1
    if count>100:
        break

if count > 100:
    print("-1")
else:
    print(count)