class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node [' + str(self.data) + ']'


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        return Node(data)

    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def mirrorTree(self, node):
        if node.left and node.right:
            node.left, node.right = node.right, node.left
            self.mirrorTree(node.right)
            self.mirrorTree(node.left)
        else:
            if node.left is None and node.right:
                return self.mirrorTree(node.right)
            if node.right is None and node.left:
                return self.mirrorTree(node.left)

    def lookup(self, node, target):
        if node is None:
            return 0
        else:
            if target == node.data:
                return 1
            else:
                if target < node.data:
                    return self.lookup(node.left, target)
                else:
                    return self.lookup(node.right, target)

    def getMaxWidth(self, root):
        maxWdth = 0
        i = 1
        h = self.height(root)
        while i < h:
            width = self.getWidth(root, i)
            if width > maxWdth:
                maxWdth = width
            i += 1
        return maxWdth

    def getWidth(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.getWidth(root.left, level - 1) + self.getWidth(root.right, level - 1)

    def printGivenLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print("%d " % root.data)
        elif level > 1:
            self.printGivenLevel(root.left, level-1)
            self.printGivenLevel(root.right, level-1)

    def printLevelOrder(self, root):
        h = self.height(self.root)
        i = 1
        while i <= h:
            self.printGivenLevel(self.root, i)
            i += 1

tree = Tree()
for x in [7, 3, 2, 1, 9, 5, 4, 6, 8]:
    tree.add(x)
tree.printLevelOrder(0)
