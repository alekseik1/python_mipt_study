from collections import deque

def sp(a):
    A = []
    if int(a[0])-2 > 0 and int(a[1])-1 > 0:
        b=str(int(a[0])-2)+str(int(a[1])-1)
        A.append(b)
    if int(a[0])-2 > 0 and int(a[1])+1 <= 8:
        b=str(int(a[0])-2)+str(int(a[1])+1)
        A.append(b)
    if int(a[0])+2 <= 8 and int(a[1])-1 > 0:
        b=str(int(a[0])+2)+str(int(a[1])-1)
        A.append(b)
    if int(a[0])+2 <= 8 and int(a[1])+1 <= 8:
        b=str(int(a[0])+2)+str(int(a[1])+1)
        A.append(b)
    if int(a[0])-1 > 0 and int(a[1])-2 > 0:
        b=str(int(a[0])-1)+str(int(a[1])-2)
        A.append(b)
    if int(a[0])-1 > 0 and int(a[1])+2 <= 8:
        b=str(int(a[0])-1)+str(int(a[1])+2)
        A.append(b)
    if int(a[0])+1 <= 8 and int(a[1])-2 > 0:
        b=str(int(a[0])+1)+str(int(a[1])-2)
        A.append(b)
    if int(a[0])+1 <= 8 and int(a[1])+2 <= 8:
        b=str(int(a[0])+1)+str(int(a[1])+2)
        A.append(b)
    return A

def rename(A1):
    if A1[0]=='a':
        A1 = '1'+A1[1]
        return(A1)
    if A1[0]=='b':
        A1 = '2'+A1[1]
        return(A1)
    if A1[0]=='c':
        A1 = '3'+A1[1]
        return(A1)
    if A1[0]=='d':
        A1 = '4'+A1[1]
        return(A1)
    if A1[0]=='e':
        A1 = '5'+A1[1]
        return(A1)
    if A1[0]=='f':
        A1 = '6'+A1[1]
        return(A1)
    if A1[0]=='g':
        A1 = '7'+A1[1]
        return(A1)
    if A1[0]=='h':
        A1 = '8'+A1[1]
        return(A1)

def rerename(A1):
    if A1[0]=='1':
        A1 = 'a'+A1[1]
        return(A1)
    if A1[0]=='2':
        A1 = 'b'+A1[1]
        return(A1)
    if A1[0]=='3':
        A1 = 'c'+A1[1]
        return(A1)
    if A1[0]=='4':
        A1 = 'd'+A1[1]
        return(A1)
    if A1[0]=='5':
        A1 = 'e'+A1[1]
        return(A1)
    if A1[0]=='6':
        A1 = 'f'+A1[1]
        return(A1)
    if A1[0]=='7':
        A1 = 'g'+A1[1]
        return(A1)
    if A1[0]=='8':
        A1 = 'h'+A1[1]
        return(A1)

def bfs(start):
    q = deque()
    visited = set()
    q.append(start)
    visited.add(start)
    dist = dict()
    dist[start] = 0
    p = dict()
    while q:
        current = q.popleft()
        for next in sp(current):
            if next not in visited:
                p[next] = current
                dist[next] = dist[current] + 1
                q.append(next)
                visited.add(next)
    return p

A1= input()
A1=rename(A1)

A2= input()
A2=rename(A2)

ans = []
order = bfs(A1)
vertex = A2
while vertex != A1:
    ans.append(vertex)
    vertex = order[vertex]

ans = ans[::-1]
print(rerename(A1))
for i in range(len(ans)):
    ans[i] = rerename(ans[i])
    print(ans[i])
