class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    res = []
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

    def print(self, root="first_iter"):
        if root == "first_iter":
            root = self.root
        if root is None:
            return
        if root.left is not None:
            self.print(root.left)
        print(root.data, end=" ")
        if root.right is not None:
            self.print(root.right)
        #if (root.right is None) and (root.left is None):
        #    self.res.append(root)

    def check(self, root='f'):
        if root == 'f':
            root = self.root
        if (root.left is None) and (root.right is None):
            self.res.append(root)
        if root.left is not None:
            self.check(root.left)
        if root.right is not None:
            self.check(root.right)

tree = Tree()
for x in list(map(int, input().split())):
    tree.add(x)
tree.check()
for i in tree.res:
    print(i.data, end=' ')