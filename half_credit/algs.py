class Graph:

    graph_as_matrix = []
    graph_as_list = []
    number_of_components = 1
    dfs_used = None
    bfs_fired = None
    spanning_tree = []
    bfs_time = {}

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
        return self.dfs_used                            # Итак, мы прошли по всей компоненте связности и ни разу не отметили никого два раза.

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

g = Graph()
g.read_graph_as_lists()
print(g.count_components_bfs())
