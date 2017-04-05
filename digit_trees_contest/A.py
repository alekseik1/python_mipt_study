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