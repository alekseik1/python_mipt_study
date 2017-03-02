class Graph:

    circles = 0

    def __init__(self, G, G_n):
        self.G = G
        self.G_n = G_n

    def dijkstra(self, start):
        d = {v: float('+inf') for v in self.G}
        d[start] = 0
        used = set()
        path = [[start] for x in range(len(self.G))]
        while len(used) != len(self.G):
            min_d = float('+inf')
            for v in d:
                if d[v] < min_d and v not in used:
                    current = v
                    min_d = d[v]
                    path[v] += [current]
            used.add(current)
            for neighbour in self.G[current]:
                l = d[current] + self.G[current][neighbour]
                if l < d[neighbour]:
                    d[neighbour] = l
                    path[neighbour] = path[current] + [neighbour]
        return d, path

    def dijkstra_for_one(self, start, stop):
        d = {v: float('+inf') for v in self.G}
        d[start] = 0
        used = set()
        path = [[start] for x in range(len(self.G))]
        while len(used) != len(self.G):
            min_d = float('+inf')
            for v in d:
                if d[v] < min_d and v not in used:
                    current = v
                    min_d = d[v]
                    path[v] += [current]
            used.add(current)
            for neighbour in self.G[current]:
                l = d[current] + self.G[current][neighbour]
                if l < d[neighbour]:
                    d[neighbour] = l
                    path[neighbour] = path[current] + [neighbour]
                    if neighbour == stop:
                        return d[neighbour]
        return d, path

    def get_neighbours(self, v):
        return list(self.G_n[v].keys())

    def _where_can_go_to_vertex(self, vertex):
        l = self.get_neighbours(vertex)
        res = []
        for i in l:
            try:
                if self.G[i][i]:
                    res.append(i)
            except:
                1==1
        return res

    def find_shortest_circle_length(self, v):
        self.dijkstra(v)

    def bfs_fire(self, start, fired=None):
        if fired is None:
            fired = set()
        fired.add(start)
        Q = [start]
        while Q:
            current = Q.pop(0)
            for neighbour in self.G[current]:
                if neighbour not in fired:
                    fired.add(neighbour)
                    Q.append(neighbour)
                    #print(current, neighbour)
                else:
                    self.circles += 1
        if self.circles == 0:
            return False

    def circles_from_vertex(self, start, fired=None):
        if fired is None:
            fired = set()
        fired.add(start)
        Q = [start]
        while Q:
            current = Q.pop(0)
            for neighbour in self.G[current]:
                if neighbour not in fired:
                    fired.add(neighbour)
                    Q.append(neighbour)
                    #print(current, neighbour)
                else:
                    return True
        return False

    def count_circles(self):
        for i in range(len(self.G)):
            self.bfs_fire(i)
        return self.circles

    def count_least_circle(self):
        res = dict()
        for i in range(len(self.G)):
            if self.circles_from_vertex(i):
                for j in self._where_can_go_to_vertex(i):
                    res.update({i: {j, self.dijkstra_for_one(i, j)+1}})
        result = []
        tmp = 0
        for i in range(len(res)):
            for j in res[i]:
                if res[i][j] < tmp:
                    tmp = res[i][j]
                    result = [i, j]
        return result

    def find_path(self):
        a = self.count_least_circle()
        d, path = self.dijkstra(G, a[0])
        path[a[1]] = [e for j, e in enumerate(path[a[1]]) if e not in path[a[1]][:j]]
        print(*path[a[1]])

n, m = [int(x) for x in input().split()]
G = {x: {} for x in range(n)}
G_nonstrict = {x: {} for x in range(n)}
for i in range(m):
    a, b = [int(x) for x in input().split()]
    G[a][b] = 1
    G_nonstrict[a][b] = 1
    G_nonstrict[b][a] = 1
G = Graph(G, G_nonstrict)
#print(G.get_neighbours(1))
G.count_circles()
if G.circles == 0:
    print('NO CYCLES')
else:
    G.find_path()