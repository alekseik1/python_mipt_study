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

    def print(self):
        if self.root is None:
            return

        Q = [self.root]
        while Q:
            root = Q.pop(0)
            print(root.data, end=" ")
            if root.left is not None:
                Q.append(root.left)
            if root.right is not None:
                Q.append(root.right)


tree = Tree()
for x in map(int, input().split()):
    tree.add(x)
tree.print()
