class Graph():
    graph_as_list = []
    graph_as_list_reverse = []
    graph_as_matrix = []
    dfs_used = set()
    number_of_components = 0
    B = set()
    B1 = set()
    N, M = 0, 0

    def read_graph_as_list(self):
        self.N = int(input())
        self.M = int(input())
        res = [[] for i in range(self.N)]
        for edge in range(self.M):
            a, b = [int(x) for x in input().split()]
            res[a].append(b)
            res[b].append(a)
        self.graph_as_list = res

    def read_strong_graph_as_list(self):
        self.N = int(input())
        self.M = int(input())
        res = [[] for i in range(self.N)]
        res1 = [[] for j in range(self.N)]
        for edge in range(self.M):
            a, b = [int(x) for x in input().split()]
            res[a].append(b)
            res1[b] += [a]
        self.graph_as_list = res
        self.graph_as_list_reverse = res1

    def dfs(self, vertex, graph, used):
        self.call_all_friends(vertex, graph, used)

    def count_components(self):
        for vertex in range(self.N):
            if vertex not in self.dfs_used:
                self.dfs(vertex, self.graph_as_list, self.dfs_used)
                self.number_of_components += 1

    def check_strong(self):
        self.call_all_friends(0, self.graph_as_list, self.B)
        n = len(self.B)
        self.call_all_friends(0, self.graph_as_list_reverse, self.B1)
        k = len(self.B1)
        if n == k:
            return True
        else:
            return False

    def call_all_friends(self, me, friends, already_called=set()):
        already_called.add(me)
        for friend in friends[me]:
            if friend not in already_called:
                self.call_all_friends(friend, friends, already_called)


A = Graph()
A.read_strong_graph_as_list()
if A.check_strong():
    print('YES')
else:
    print('NO')
