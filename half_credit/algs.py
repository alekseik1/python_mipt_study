class Graph:
    """
    Класс graph для работы с графами. Умеет многое, но не все: функционал будет расширяться по мере необходимости
    """

    graph_as_matrix = []    # Граф в виде матрицы смежности
    graph_as_matrix_weight = [] # То же самое, но с весами
    graph_as_matrix_weight_for_kraskal = []
    graph_as_list = []      # Граф в виде списка смежности
    number_of_components = 1    # Число компонент связности графа
    dfs_used = None
    N, M = 0, 0
    spanning_tree_dfs = []
    bfs_fired = None
    spanning_tree = []      # Остовное дерево графа. Имеет не очень хороший вид, пример: [[1, 2], [2, 3]], где 1, 2, 3 - вершины
    bfs_time = {}           # Время поджига bfs, т.е. на какой итерации bfs_fire какая вершина загорелась. Имеет стркутуру словаря

    # 1
    def read_graph_as_matrix(self):
        '''
        Считывает граф как матрицу смежности, т.е. A[0][1] будет 1, если есть путь из 0 в 1.
        @return: Возвращает матрицу смежности, а также записывает ее в поле graph_as_matrix
        '''
        N, M = [int(x) for x in input().split()]
        self.N, self.M = N, M
        graph = [[0] * N for i in range(N)]  # матрица смежностей
        for edge in range(M):
            a, b = [int(x) for x in input().split()]
            graph[a][b] = 1             # Здесь можно было записывать вес, см. ниже
            graph[b][a] = 1             # А этой строки не должно быть, если граф ориентирован!
        self.graph_as_matrix = graph    # Записываем в поле экземпляра
        return graph                    # Возвращаем как результат

    # 1
    def read_graph_as_matrix_weight(self):
        '''
        Считывает взвешенный граф как матрицу смежности, т.е. A[0][1] будет x, если есть путь из 0 в 1 с весом x.
        @return: Возвращает матрицу смежности в виде списка в списке, а также записывает ее в поле graph_as_matrix_weight.
        '''
        N, M = [int(x) for x in input().split()]
        self.N, self.M = N, M
        graph = {v: {k: float('+inf') for k in range(N)} for v in range(N)}
        for edge in range(M):
            a, b, c = [int(x) for x in input().split()]
            graph[a][b] = c             # Здесь можно было записывать вес, см. ниже
            graph[b][a] = c             # А этой строки не должно быть, если граф ориентирован!
            self.graph_as_matrix_weight_for_kraskal.append((c, a, b))
        self.graph_as_matrix_weight = graph    # Записываем в поле экземпляра
        return graph                    # Возвращаем как результат

    # 1
    def read_graph_as_lists(self):
        '''
        Считывает граф как лист "смежности", т.е. A[0] будет списком из всех вершин, смежных с вершиной 0
        @return: Возвращает лист, а также записывает его в поле graph_as_list
        '''
        N, M = [int(x) for x in input().split()]
        self.N, self.M = N, M
        graph = [[] for i in range(N)]
        for edge in range(M):
            a, b = [int(x) for x in input().split()]
            graph[a].append(b)  # Полная аналогия с методом выше
            graph[b].append(a)  # Для ориентированного графа строка не нужна
        self.graph_as_list = graph
        return graph

    def print2d(self):
        '''
        Печатает граф в виде последовательности строк. Просто и со вкусом
        @return: Возвращает 0
        '''
        for line in self.graph_as_matrix:
            print(*line)
        print()
        return 0

    def dfs_list_graph(self, vertex=0):  # Depth-first search - в глубину
        """
        Обход графа в глубину для графа, заданного листом. Вершины, которые обошли, будут записаны в поле dfs_used
        @param vertex: Вершина, с которой начнется обход
        @return: Возвращает массив dfs_used, а также записывает его в поле класса (dfs_used, то же имя)
        """
        if self.dfs_used is None:   # Первый запуск - нам нужно сделать это пустым множеством
            self.dfs_used = set()
        self.dfs_used.add(vertex)                       # Сначала добавляем вершину в список прогнанных, а затем
        for neighbour in self.graph_as_list[vertex]:    # для каждого её соседа,
            if neighbour not in self.dfs_used:          # если его мы не прогоняли по нашему алгоритму, то
                self.dfs_list_graph(neighbour)          # запускаем прогонку с началом в этом соседе.
                self.spanning_tree_dfs.append([vertex, neighbour])  # Делаем остовное дерево. Внимание, его нужно после прогона отсортировать!
        return self.dfs_used                            # Итак, мы прошли по всей компоненте связности и ни разу не отметили никого два раза.

    # 4
    def get_spanning_tree_dfs(self):
        """
        Ищет остовное дерево, начиная с 0 вершины, через обход в глубину
        @return: Возвращает лист остовного дерева вида [[0, 1], [1, 2] ... ]
        """
        self.dfs_list_graph()
        return sorted(self.spanning_tree_dfs)

    # 2
    def count_components_dfs(self):
        """
        Считает количество компонент связности в графе, заданном листом, с помощью обхода в глубину.
        @return: Возвращает число - количество компонент связности, а также записывает его в поле number_of_components
        """
        if self.dfs_used is None:   # Если мы ни разу не считали компоненты, чтобы in self.dfs_used ниже в проверке не вылетал :)
            self.dfs_used = set()

        n = 0
        for vertex in range(len(self.graph_as_list)):   # Для каждой вершины,
            if vertex not in self.dfs_used:             # если она не была обработана dfs, то
                self.dfs_list_graph(vertex)             # обрабатываем все вершины функцией dfs, начиная с vertex,
                n += 1                                  # и увеличиваем число компонент на 1
        self.number_of_components = n                   # записываем результаты трудов
        return n

    def bfs_fire_list_graph(self, start):       # TODO: сделать адекватный spanning tree
        """
        "Поджиг КПМ" по Хирьянову или же просто обход графа в ширину.
        @param start: откуда начинать
        @return: Возвращает множество из зажженных вершин
        """
        if self.bfs_fired is None:      # Первая инициализация
            self.bfs_fired = set()

        self.bfs_fired.add(start)       # Мы зажгли первую вершину
        time = {start: 0}      # Хранение времен их добывания, потом мы увидим, что это может пригодиться
        Q = [start]     # Очередь на зажигание
        while Q:                                                # Пока очередь не опустошилась:
            current = Q.pop(0)                                  # Берем самого верхнего из очереди и начинаем
            for neighbour in self.graph_as_list[current]:       # для каждого его соседа,
                if neighbour not in self.bfs_fired:             # если он не был "подожжен",
                    self.bfs_fired.add(neighbour)               # "поджигаем" его и
                    Q.append(neighbour)                         # добавляем этого несчастного соседа в очередь, чтобы в следующей итерации уже поджигать его соседей
                    # Все это дело закончится, когда все соседи, до которых мы дотянемся, будут зажжены
                    #print(current, neighbour)  # А вот тут мы пишем, от кого куда пришло пламя. Если это записать в массив, то можно получить остовное дерево
                    self.spanning_tree.append([current, neighbour])
                    time[neighbour] = time[current] + 1
        self.bfs_time = time
        return self.bfs_fired

    # 5
    def get_spanning_tree_bfs(self, vertex=0):
        """
        Ищет остовное дерево, начиная с вершины vertex, с помощью обхода в ширину
        @return: Возвращает лист вида [[0, 1], [1, 2] ... ]
        """
        if self.bfs_fired is None:
            self.bfs_fire_list_graph(vertex)
        return self.spanning_tree

    # 3
    def count_components_bfs(self):
        """
        Считает количество компонент связности в графе, заданном листом, через обход в ширину.
        @return: Возвращает число - количество компонент связности, а также записывает его в поле number_of_components
        """

        if self.bfs_fired is None:   # Если мы ни разу не считали компоненты, чтобы in self.bfs_fired ниже в проверке не вылетал :)
            self.bfs_fired = set()
        number_of_components = 0

        for vertex in range(len(self.graph_as_list)):       # Для каждой вершины,
            if vertex not in self.bfs_fired:                # если она не была обработана dfs, то
                self.bfs_fire_list_graph(vertex)            # обрабатываем все вершины функцией dfs, начиная с vertex,
                number_of_components += 1                   # и увеличиваем число компонент на 1
        self.number_of_components = number_of_components    # записываем результаты трудов
        return self.number_of_components

    # 6
    def get_shortest_paths_from_vertex(self, start):
        """
        Поиск кратчайших путей из заданной вершины до всех остальных с помощью алгоритма Дейкстры. Граф должен быть
        задан с помощью read_graph_as_matrix_weight
        @param start: Вершина, из которой считаем пути
        @return: Лист из длин путей
        """

        if self.graph_as_matrix_weight is []:
            raise AssertionError("Граф должен быть задан через метод read_graph_as_matrix_weight()")

        d = {v: float('+inf') for v in self.graph_as_matrix_weight}     # Сначала везде путь - бесконечность
        paths = {v: [] for v in self.graph_as_matrix_weight}            # Пустые пути
        d[start] = 0    # До начальной точки путь имеет длину 0
        used = set()    # Инициализация
        while len(used) != len(self.graph_as_matrix_weight):                        # Пока все вершины не помечены:
            min_d = float('+inf')                                                   # Сначала min_d есть бесконечность
            for v in d:                                                             # для каждой вершины из графа,
                if d[v] < min_d and v not in used:                                  # если текущий кратчайший путь до нее меньше min_d и эту вершину мы еще не пометили
                    current = v                                                     # устанавливаем эту вершину как "рабочую"
                    min_d = d[v]                                                    # устанавливаем текущий минимум на кратчайший путь до "рабочей" вершины,
                                                                                    # таким образом, в конце цикла мы имеем: current - наша "рабочая" вершина - указывает на непомеченную вершину с минимальным путем из start, а min_d - на длину этого пути
            paths[current] += [current]
            used.add(current)                                                       # закидываем "рабочую" вершину в помеченные
            for neighbour in self.graph_as_matrix_weight[current]:                  # для каждого соседа "рабочей" вершины:
                l = d[current] + self.graph_as_matrix_weight[current][neighbour]    # а могли ли мы более выгодно прийти в соседа из "рабочей" вершины через одно ребро?
                if l < d[neighbour]:                                                # считаем путь в таком случае и сверяем с текущим минимальным путем до соседа
                    d[neighbour] = l                                                # если оказался меньше, то обновляем значение
                    paths[neighbour] = paths[current] + [neighbour]                 # и делаем путь до этого соседа следующим: путь до "рабочей" вершины + сосед

        for i in range(1, len(paths)):                                              # Но тут проблема: в листе пути повторяются точки. Мы уберем повторения в цикле
            j = 0                                                                   # Для каждого пути
            while True:
                if paths[i][j] == paths[i][j+1]:                                    # Если совпадает со следующим, удаляем
                    paths[i].pop(j)
                    j = 0
                    continue
                j += 1
                if j == len(paths[i])-1:                                            # Организация счетчика
                    break
        return d, paths

    # 7
    # TODO: Сделать для любой вершины в качестве начальной
    def get_shortest_paths_by_floyd_vershel(self, start=0):
        """
        Возвращает кратчайшие пути до всех вершин, начиная с 0, через алгоритм Флойда-Уоршелла. НЕ СПОСОБЕН считать для других вершин в качестве начальной, простите, я это не успел написать
        @param start: Начальная вершина, пока НЕ работает
        @return: Лист из путей до вершин
        """
        INF = 10**11
        n = self.N
        A = [[[INF] * n for i in range(n)] for k in range(n + 1)]  # INF - условная бесконечность, n - число ребер
        W = [[self.graph_as_matrix_weight[i][j] for j in range(self.N)] for i in range(self.N)]     # Супер-массив, строится по правилу: W[i][j] - вес пути из i в j
        for i in range(self.N): W[i][i] = 0     # Путь из i в i есть 0
        for i in range(n):
            A[0][i][:] = W[i]  # При копировании весовой матрицы W расстояние от вершины до себя равно нулю; забиваем матрицу рёбер т.е.расстояния в начальный момент.
        for k in range(1, n):                                                          # пусть A[k][i][j] - кратчайший путь из i в j, проходящий через ребра с номерами 1..k (помимо самих i и j, естественно)
            for i in range(n):                                                         # тогда, если кратчайший путь из i в j не проходит через k, то A[k][i][j] = A[k-1][i][j] - в самом деле, разницы между ними нет, т.к. путь не проходит через k
                for j in range(n):                                                     # либо же есть более короткий путь, но тогда он проходит сначала от i до k через (k-1) вершину, а затем из k в j,
                    A[k][i][j] = min(A[k - 1][i][j], A[k - 1][i][k] + A[k - 1][k][j])  # в этом случае A[k][i][j] = A[k-1][i][k] + A[k-1][k][j]
                                                                                       # Мы все это дело проверяем в цикле и выдаем как результат лист A[n-1][start] (да, это лист, потому что А - трехмерный массив, во как!)
        return A[n-1][start]

    # 8
    # TODO: В качестве свистоперделки можно сделать возможность обхода с произвольной вершины, а не только 0.
    # TODO: Да и вообще, нужно его нехило переделать, ибо он ломается, если путь 0-1 не является кратчайшим на первой итерации.
    # TODO: Есть предожение подавать ему на вход топологически отсортированный граф, но ведь это уже костыли!
    def get_min_spinning_tree_by_prim(self):
        """
        Строит остовное дерево минимального веса с помощью алгоритма Прима. Начинает обход с вершины 0
        @return: Возвращает остовное дерево минимального веса в виде листа вида [[0, 1], [1, 2] ... ]
        """
        INF = 10 ** 9  # Введем условную бесконечность
        dist = [INF] * self.N  # W[i][j] - вес ребра ij, который равен +бесконечность, если i не смежна j
        W = [[self.graph_as_matrix_weight[i][j] for j in range(self.N)] for i in range(self.N)]     # Супер-массив, строится по правилу: W[i][j] - вес пути из i в j
        dist[0] = 0
        used = [False] * self.N
        used[0] = True
        tree = []
        tree_weight = 0
        u = 1
        for i in range(self.N):                         # Поехали! Для каждой вершины i из графа делаем следующую магию:
            min_d = INF
            for j in range(self.N):                     # Для каждой j из вершин графа
                if not used[j] and dist[j] < min_d:     # если мы не отметили эту вершину и расстояние до ее меньше min_d, то
                    min_d = dist[j]                     # обновляем min_d
                    u = j                               # и ставим метку на эту вершину
                                                        # Итог: мы выбрали непомеченную вершину с минимальным расстоянием от i. Назовем ее "избранной"
            if min_d == INF:
                min_d = W[0][u]
            tree.append((i, u))                         # Добавляем эту вершину в дерево
            tree_weight += min_d                        # и расстояние до нее - в конечный вес дерева
            used[u] = True                              # ну, и делаем вершину помеченной :)
            for v in range(self.N):                     # Самый сок: для каждой вершины v мы записываем в минимальное расстояние до нее следующее -
                dist[v] = min(dist[v], W[u][v])         # минимум из текущего минимального расстояния и веса от "избранной" к v. Это повзолит также избавиться от бесконечностей, которые мы в начале прописали
        # На вики есть хорошее и наглядное объяснение, если не понятно, можете загуглить)
        return tree, tree_weight

    # 9
    def get_min_spinning_tree_by_kraskal(self):
        """
        Ищет остовное дерево минимальной длины с помощью алгоритма Краскала.
        @return: Возвращает лист вида [[0, 1], [1, 2] ... ]
        """
        N, M = self.N, self.M
        edges = self.graph_as_matrix_weight_for_kraskal         # Уютно записанные ребра вида [(1, 0, 1), ...], где первое число - вес, второе - откуда, третье - куда, т.о. 1 - вес при прогулке от 0 до 1
        edges.sort()                                            # Сортируем их
        comp = list(range(N))                                   # Ууу, тут большое колдунство с компонентой, но я постараюсь объяснить
        tree = []                                               # Сначала дерево пусто
        tree_weight = 0                                         # Как и его вес
        for weight, v1, v2 in edges:                            # А теперь, для каждых пар вершин и веса при переходе между ними
            if comp[v1] != comp[v2]:                            # Если две эти вершины лежат в разных компонентах (см. ниже, первоначально они все лежат в разных компонентах)
                tree.append((v1, v2))                           # то мы в дерево добавляем эти вершины
                tree_weight += weight                           # увеличиваем вес дерева
                for i in range(N):                              # а вот теперь, для i
                    if comp[i] == comp[v2]:                     # если компонента i-ая равна компоненте второй вершины
                        comp[i] = comp[v1]                      # то мы в эту i-ую компоненту записываем comp[v1]
                                                                # Что это нам дает? Мы тут проходим по РЕБРАМ, так что не факт, что мы после первой-второй итерации вообще получим что-то связное. Поэтому и нужны компоненты
                                                                # А поскольку веса отсортированы, мы гарантированно добавляем в дерево наименьшие ребра,
                                                                # но перед этим мы проверяем, не замкнет ли ребро цикл. Как? Проверкой компонент, разумеется, вон же, выше (if comp[v1] != comp[v2])
                                                                # А когда ребро добавляется в дерево, его компонента становится равна компоненте всего дерева, вот и все.

# Тестирование класса, пожалуйста, не обращайте внимания на этот код
g = Graph()
g.read_graph_as_matrix_weight()
print(g.get_shortest_paths_from_vertex(0))
print(g.get_shortest_paths_by_floyd_vershel())
print(g.get_min_spinning_tree_by_prim())
print(g.get_min_spinning_tree_by_kraskal())