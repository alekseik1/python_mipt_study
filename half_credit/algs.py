class Graph:
    """
    Класс graph для работы с графами. Умеет многое, но не все: функционал будет расширяться по мере необходимости
    """

    graph_as_matrix = []    # Граф в виде матрицы смежности
    graph_as_matrix_weight = [] # То же самое, но с весами
    graph_as_list = []      # Граф в виде списка смежности
    number_of_components = 1    # Число компонент связности графа
    dfs_used = None
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
        @return: Возвращает матрицу смежности в виде списка в списке, а также записывает ее в поле graph_as_matrix_weight
        '''
        N, M = [int(x) for x in input().split()]
        graph = {v: {k: float('+inf') for k in range(N)} for v in range(N)}
        for edge in range(M):
            a, b, c = [int(x) for x in input().split()]
            graph[a][b] = c             # Здесь можно было записывать вес, см. ниже
            graph[b][a] = c             # А этой строки не должно быть, если граф ориентирован!
        self.graph_as_matrix_weight = graph    # Записываем в поле экземпляра
        return graph                    # Возвращаем как результат

    # 1
    def read_graph_as_lists(self):
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


# Тестирование класса, пожалуйста, не обращайте внимания на этот код
g = Graph()
g.read_graph_as_matrix_weight()
print(g.get_shortest_paths_from_vertex(0))
#g.read_graph_as_matrix_weight()
#print(g.bfs_fire_list_graph(0))
#print(g.spanning_tree)
#print(g.get_shortest_paths_from_vertex(0))
