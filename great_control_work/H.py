n = int(input())
l = [0]*n
for i in range(n):
    l[i] = [int(x) for x in input().split()]


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
nodes = []
for i in range(len(l)):
    left = None
    right = None
    if l[i][1] != -1:
        left = Node(l[l[i][1]][0]
    if l[i][2] != -1:
        right = l[l[i][2]][0]
    nodes.append(Node(l[i][0], left, right))

print()
def check_node(node):
    if node.left is not None:
        if node.left > node.data:
            return False
    if node.right is not None:
        if node.right < node.data:
            return False
    return True
