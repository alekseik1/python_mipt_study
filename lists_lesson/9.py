N = int(input())
a = []
a.extend(map(int, input().split()))
k = int(input())
s = [0]
for i in range(N-k+1):
    s.append(sum(a[i:i+k]))
print(max(s))