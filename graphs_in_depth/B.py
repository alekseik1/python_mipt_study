class Graph():

    graph_as_list = []
    graph_as_matrix = []
    dfs_used = set()
    number_of_components = 0
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

    def dfs(self, vertex, graph, used):
        self.call_all_friends(vertex, graph, used)

    def count_components(self):
        for vertex in range(self.N):
            if vertex not in self.dfs_used:
                self.dfs(vertex, self.graph_as_list, self.dfs_used)
                self.number_of_components += 1

    def call_all_friends(self, me, friends, already_called=set()):
        already_called.add(me)
        for friend in friends[me]:
            if friend not in already_called:
                self.call_all_friends(friend, friends, already_called)

A = Graph()
A.read_graph_as_list()
A.count_components()

print(A.number_of_components)
