#  Алгоритм. подсказки на http://e-maxx.ru/algo/
# 1. В исходном графе Г' находятся все вершины нечетной степени, если таковых нет то п. 6.
# 2. Для каждой такой вершины находятся кратчайшие пути до всех остальных, эти пути запоминаются.
# 3. На этих вершинах строится двудольный граф Г' с весами, равными кратчайшему расстоянию (на рисунке 2 видна соответствующая матрица смежности для сэмпла)
# 4. Ищем максимальное паросочетание минимального веса.
# 5. По паросочетанию добавляем в исходный граф дополнительные ребра. Т.е. если у нас в паросочетании Г' есть ребро (A,B), то в Г добавляется цепь кратчайшего пути м/у вершинами А и В. Получаем эйлеров граф.
# 6. Находим эйлерову цепь.
# 7. PROFIT!

def readGraf():
    n, m = [int(x) for x in input().split()]
    G = {x: {} for x in range(n)}
    for i in range(m):
        a, b, w = [int(x) for x in input().split()]
        G[a][b] = w
        G[b][a] = w
    return G

def buildUpToAilerGraf(G):
    """достраивание исходного графа до эйлерова, для которого решение очевидно"""
    addedWeight = 0
    T = findTnodes(G)
    paths = []
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            paths.append((dey(G,T[i],T[j]),T[i],T[j]))
    paths.sort()
    while paths: # пока плохие вершины есть, продолжаем добавлять дублирующие рёбра
        minAddiction = paths[0]
        v1 = minAddiction[1]
        v2 = minAddiction[2]
        paths = [path for path in paths if not (path[1]==v1 or path[1]==v2 or path[2]==v1 or path[2]==v2)]
        addedWeight+=minAddiction[0]

    return addedWeight

def findTnodes(G):
    """поиск вершин нечётной кратности"""
    ret = []
    for v in G:
        if len(G[v])%2==1:
            ret.append(v)
    return ret

def dey(G,a,b):
    """дейкстра"""
    distances = [float('+inf')]*len(G)
    distances[a] = 0
    used = set()
    while len(used)!=len(G):
        min_d = float('+inf')
        for v in G:
            if v not in used and distances[v]<min_d:
                min_d = distances[v]
                curr = v
        for neibor in G[curr]:
            if neibor not in used:
                new_dist = distances[curr]+G[curr][neibor]
                if new_dist < distances[neibor]:
                    distances[neibor] = new_dist
        used.add(curr)
    return distances[b]

def basicWeight(G):
    """суммарный путь по исходному графу"""
    w = 0
    for v in G:
        for neibor in G[v]:
            w+=G[v][neibor]
    return w//2

G = readGraf()
basic = basicWeight(G)
added = buildUpToAilerGraf(G)
print(basic + added) # izi 200
'''
4 4
2 0 13
1 0 14
2 3 67
1 2 88
'''  # 249
'''
6 6
3 2 36
1 0 53
1 2 34
1 5 3
3 4 3
5 3 64
''' # 249

