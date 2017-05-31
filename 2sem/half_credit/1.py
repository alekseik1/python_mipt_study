# 1
def read_graph_as_matrix():
    '''
    Считывает граф как матрицу смежности, т.е. A[0][1] будет 1, если есть путь из 0 в 1.
    @return: Возвращает матрицу смежности, а также записывает ее в поле graph_as_matrix
    '''
    N, M = [int(x) for x in input().split()]
    graph = [[0] * N for i in range(N)]  # матрица смежностей
    for edge in range(M):
        a, b = [int(x) for x in input().split()]
        graph[a][b] = 1  # Здесь можно было записывать вес, см. ниже
        graph[b][a] = 1  # А этой строки не должно быть, если граф ориентирован!
    return graph  # Возвращаем как результат


# 1
def read_graph_as_matrix_weight():
    '''
    Считывает взвешенный граф как матрицу смежности, т.е. A[0][1] будет x, если есть путь из 0 в 1 с весом x.
    @return: Возвращает матрицу смежности в виде списка в списке, а также записывает ее в поле graph_as_matrix_weight.
    '''
    N, M = [int(x) for x in input().split()]
    graph = {v: {k: float('+inf') for k in range(N)} for v in range(N)}
    for edge in range(M):
        a, b, c = [int(x) for x in input().split()]
        graph[a][b] = c  # Здесь можно было записывать вес, см. ниже
        graph[b][a] = c  # А этой строки не должно быть, если граф ориентирован!
    return graph  # Возвращаем как результат


# 1
def read_graph_as_lists():
    '''
    Считывает граф как лист "смежности", т.е. A[0] будет списком из всех вершин, смежных с вершиной 0
    @return: Возвращает лист, а также записывает его в поле graph_as_list
    '''
    N, M = [int(x) for x in input().split()]
    graph = [[] for i in range(N)]
    for edge in range(M):
        a, b = [int(x) for x in input().split()]
        graph[a].append(b)  # Полная аналогия с методом выше
        graph[b].append(a)  # Для ориентированного графа строка не нужна
    return graph