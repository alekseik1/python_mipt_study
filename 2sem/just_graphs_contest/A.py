N, M = map(int, input().split())
Used = []
total_Used = set()
heights = [[] for i in range(N)]

for j in range(M):
    a, b = map(int, input().split())
    heights[a].append(b)

result = []
def obhod(heights, Used, element, total_Used):

    if element in Used:
        result[:] = []
        for i in range(Used.index(element), len(Used)):
            result.append(Used[i])
        return
    if element in total_Used:
        return
    current_Used = []
    current_Used[:] = Used[:] + [element]
    total_Used.add(element)
    for number in heights[element]:
        obhod(heights, current_Used, number, total_Used)
        if len(result) > 0:
            break


for n in range(N):
    if not n in total_Used:
        obhod(heights, Used, n, total_Used)

if len(result) > 0:
    print(*result)
else:
    print("YES")