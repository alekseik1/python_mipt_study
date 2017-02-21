class Graph():

    graph_as_list = []
    graph_as_matrix = []

    def read_graph_as_list(self):
        N = int(input())
        M = int(input())
        res = [[] for i in range(N)]
        for edge in range(M):
            a, b = [int(x) for x in input().split()]
            res[a].append(b)
            res[b].append(a)
        self.graph_as_list = res

    def call_all_friends(self, me, friends, already_called=set()):
        already_called.add(me)
        for friend in friends[me]:
            if friend not in already_called:
                self.call_all_friends(friend, friends, already_called)

A = Graph()
A.read_graph_as_list()
A.call_all_friends(0, A.graph_as_list)