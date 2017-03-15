n, m = map(int, input().split())  # количество вершин и ребер в графе
adj = [[] for i in range(n)]  # список смежности
color = [int(0) for i in range(n)]  # массив для хранения цветов вершин
topSort = []  # топологически упорядоченная перестановка вершин графа

# считываем граф, заданный списком ребер
for i in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)


def topologicalSort(v):  # топологическая сортировка вершин графа
    # если вершина является черной, то не производим из нее вызов процедуры
    if color[v] == 2:
        return True
    # если вершина является серой, то орграф содержит цикл, выходим из процедуры
    if color[v] == 1:
        return False
    color[v] = 1  # помечаем вершину как серую
    # запускаем обход из всех вершин, смежных с вершиной v
    for w in adj[v]:
        # вызов обхода от вершины w, смежной с вершиной v
        if not topologicalSort(w):
            return False
    color[v] = 2  # помечаем вершину как черную
    # добавляем посещенную вершину в топологический порядок
    topSort.append(v)
    return True


def run():
    cyclic = False  # флаг, показывающий содержит орграф цикл или нет
    # запускаем процедуру, которая топологически сортирует вершины графа
    for v in range(n):
        if not topologicalSort(v):
            cyclic = True
    if not cyclic:
        topSort.reverse()
        # иначе выводим топологически упорядоченную перестановку его вершин
        print(*topSort)
    else:
        print('NO')
run()