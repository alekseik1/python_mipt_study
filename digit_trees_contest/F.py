class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1

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
            curr.count += 1
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

    def print(self, root="first_iter"):
        if root == "first_iter":
            root = self.root
        if root is None:
            return
        if root.left is not None:
            self.print(root.left)
        print(root.data, root.count)
        if root.right is not None:
            self.print(root.right)
        #return self.a

tree = Tree()
for x in list(map(int, input().split())):
    tree.add(x)
tree.print()
