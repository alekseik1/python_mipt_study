class Node:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, curr, new):
        if curr.data == new.data:
            return
        if curr.data > new.data:
            if curr.left is None:
                curr.left = new
                new.parent = curr
                self._updateHeight(curr)
                return
            next = curr.left
        else:
            next = curr.right
            if next is None:
                curr.right = new
                new.parent = curr
                self._updateHeight(curr)
                return
        self._insert(next, new)

    def print(self):
        self._printNode(self.root)

    def _printNode(self, root):
        if root is None:
            return
        if root.left is not None:
            self._printNode(root.left)
        print(root.data, end=" ")
        if root.right is not None:
            self._printNode(root.right)

    def _updateHeight(self, node):
        l = node.left
        r = node.right
        h1 = h2 = 0
        if l is not None:
            h1 = l.height
        if r is not None:
            h2 = r.height
        node.height = max(h1, h2) + 1
        if node.parent is not None:
            self._updateHeight(node.parent)

    def check(self, root="first"):
        if root == "first":
            root = self.root
            if root is None:
                return 1
        l = root.left
        r = root.right
        if l is None and r is None:
            return 1
        elif l is not None and r is None:
            return l.height == 1
        elif l is None and r is not None:
            return r.height == 1
        else:
            return abs(l.height - r.height) <= 1 and self.check(l) and self.check(r)

tree = Tree()
for x in map(int, input().split()):
    tree.add(x)
if tree.check():
    print('YES')
else:
    print("NO")