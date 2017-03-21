NM = [int(x) for x in input().split()]
n, m = NM[0], NM[1]
centers = NM[2:]
graph = {v: {k: float('+inf') for k in range(n)} for v in range(n)}
for edge in range(m):
    a, b, c = [int(x) for x in input().split()]
    graph[a][b] = c  # Здесь можно было записывать вес, см. ниже
    graph[b][a] = c  # А этой строки не должно быть, если граф ориентирован!

comp = {v: centers[0] for v in range(n)}    # Сначала все города принадлежат первом столице

def get_shortest_paths_from_vertex(start):
    d = {v: float('+inf') for v in graph}  # Сначала везде путь - бесконечность
    d[start] = 0  # До начальной точки путь имеет длину 0
    used = set()  # Инициализация
    while len(used) != len(graph):  # Пока все вершины не помечены:
        min_d = float('+inf')  # Сначала min_d есть бесконечность
        for v in d:  # для каждой вершины из графа,
            if d[v] < min_d and v not in used:  # если текущий кратчайший путь до нее меньше min_d и эту вершину мы еще не пометили
                current = v  # устанавливаем эту вершину как "рабочую"
                min_d = d[v]  # устанавливаем текущий минимум на кратчайший путь до "рабочей" вершины,
                # таким образом, в конце цикла мы имеем: current - наша "рабочая" вершина - указывает на непомеченную вершину с минимальным путем из start, а min_d - на длину этого пути
        used.add(current)  # закидываем "рабочую" вершину в помеченные
        for neighbour in graph[current]:  # для каждого соседа "рабочей" вершины:
            l = d[current] + graph[current][neighbour]  # а могли ли мы более выгодно прийти в соседа из "рабочей" вершины через одно ребро?
            if l < d[neighbour]:  # считаем путь в таком случае и сверяем с текущим минимальным путем до соседа
                d[neighbour] = l  # если оказался меньше, то обновляем значение
    return d

for city in range(n):
    d = get_shortest_paths_from_vertex(city)
    curr = 0
    for cap in centers:
        if d[cap] <= d[curr]:
            curr = cap
    # На выходе curr - минимальная из столиц (по расстоянию)
    comp[city] = curr
for i in range(n):
    print(comp[i])
