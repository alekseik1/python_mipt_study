class LinkedList:
    def __init__(self):
        self._link=None

    def __str__(self):
        p = self._link
        s = ''
        while p:
            s += str(p[0]) + ' '
            p = p[1]
        return s

    def push_front(self, data):
        self._link = [data, self._link]

    def empty(self):
        return not(self._link)

    def pop(self,data):
        '''
        Извлекает из списка связности элемент со значением data.
        При отстутствии элемента возвращает None
        '''
        p = self._link
        if p == None:
            return None
        else:
            k = None
            f = p
            while p and p[0]!=data:
                f = p
                p = p[1]
            if p and p[0]==data:
                k = data
                if f!=p:
                    f[1] = p[1]
                else:
                    self._link = p[1]
            return k
    def front(self):
        '''
        Функция возвращающая крайний элемент списка связности, при его наличии.
        Элемент не удаляется.
        При пустом списке возвращает None
        '''
        if self.empty():
            return None
        else:
            return self._link[0]

vertexes = LinkedList()

def dfs_straight(vertex, graph, used = set()):
    '''Процедура обходы прямого графа,
    с записью вершиин в глобальный стек vertexes (вершина добавляется в стек сразу после того как становится черной)
    '''
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs_straight(neighbour, graph, used)
    vertexes.push_front(vertex)


def dfs_reverse(vertex, graph, used = set()):
    '''
    Обход транспонированного графа, с удалением посещенных
    вершин из глобального стека vertexes
    '''
    used.add(vertex)
    vertexes.pop(vertex)
    linked_components[k].add(vertex) # глобальный массив множеств вершин отдельных сильносвязных компонент (*)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs_reverse(neighbour, graph, used)

N = int(input())
M = int(input())

graph = [[] for i in range(N)]
graph_full = [[] for i in range(N)]
graph_T = [[] for i in range(N)]

for edge in range(M):
    a, b = [int(x) for x in input().split()]

    graph[a].append(b)

    graph_T[b].append(a)

    graph_full[a].append(b)
    graph_full[b].append(a)

used = set()
for vertex in range(N):
    if vertex not in used:
        dfs_straight(vertex, graph, used)

linked_components = [] # (*)

k = -1
used = set()

while not vertexes.empty(): # обход вершин в G^T в порядке убывания временных меток
    k += 1
    linked_components.append(set())
    vertex = vertexes.front()
    dfs_reverse(vertex, graph_T, used)

used = set()
components = 0
for vertex in range(N):
    if vertex not in used:
        dfs_straight(vertex, graph_full, used)
        components += 1

print(components,len(linked_components))