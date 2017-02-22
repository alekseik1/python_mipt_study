class Graph():
    graph_as_list = []
    graph_as_list_nonstrict = []
    graph_as_list_reverse = []
    graph_as_matrix = []
    dfs_used = set()
    bad_dots = {0}
    number_of_components = 0
    number_of_nonstrict_components = 0
    B = set()
    B1 = set()
    N, M = 0, 0

    def read_graph_as_list(self):
        self.N = int(input())
        self.M = int(input())
        res = [[] for i in range(self.N)]
        for edge in range(self.M):
            a, b = [int(x) for x in input().split()]
            res[a].add(b)
            res[b].add(a)
        self.graph_as_list_nonstrict = res
        self.graph_as_list = res

    def kostil(self):
        res = []
        for i in self.graph_as_list_nonstrict:
            res.append(list(set(i)))
        self.graph_as_list_nonstrict = res

    def read_strong_graph_as_list(self):
        self.N = int(input())
        self.M = int(input())
        res = [[] for i in range(self.N)]
        res1 = [[] for j in range(self.N)]
        res2 = [[] for i in range(self.N)]
        for edge in range(self.M):
            a, b = [int(x) for x in input().split()]
            res[a].append(b)
            res1[b] += [a]
            res2[a].append(b)
            res2[b].append(a)
        self.graph_as_list = res
        self.graph_as_list_reverse = res1
        self.graph_as_list_nonstrict = res2

    def dfs(self, vertex, graph, used):
        self.call_all_friends(vertex, graph, used)

    def count_components(self):
        for vertex in range(self.N):
            if vertex not in self.dfs_used:
                self.dfs(vertex, self.graph_as_list, self.dfs_used)
                self.number_of_components += 1
        return self.number_of_components

    def check_strong(self, vertex=0):
        self.call_all_friends(vertex, self.graph_as_list, self.B)
        n = len(self.B)
        self.call_all_friends(vertex, self.graph_as_list_reverse, self.B1)
        k = len(self.B1)
        if n == k:
            return True
        else:
            return False

    # Возвращает список, типа [0, 1] - ноль сильных и 1 слабый
    def count_strong_components(self):
        strong = 0
        for vertex in range(self.N):
            if self.check_strong(vertex):
                strong += 1
        return strong

    def call_all_friends(self, me, friends, already_called=set()):
        already_called.add(me)
        for friend in friends[me]:
            if friend not in already_called:
                self.call_all_friends(friend, friends, already_called)


A = Graph()
A.read_strong_graph_as_list()
A.kostil()
n = A.count_components()


A.graph_as_list = A.graph_as_list_nonstrict
k = A.count_components()

for i in range(A.N):
    if not A.check_strong(i):
        k += 1
if k == 0:
    k = 1
print(k, n)
