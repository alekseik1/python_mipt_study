n = int(input())
l = [0]*n
for i in range(n):
    l[i] = [int(x) for x in input().split()]


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, curr, data):
        if curr.data == data:
            return
        if curr.data > data:
            next = curr.left
            if next is None:
                curr.left = Node(data)
                return
        else:
            next = curr.right
            if next is None:
                curr.right = Node(data)
                return
        self._insert(next, data)

