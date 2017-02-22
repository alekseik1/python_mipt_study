import random

class growing_heap:

    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def add(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1
        parent = (i - 1) / 2
        while i > 0 and self.heap[parent] < self.heap[i]:
            temp = self.heap[i]
            self.heap[i] = self.heap[parent]
            self.heap[parent] = temp

            i = parent
            parent = (i - 1) / 2

    def heapify(self, i):
        while True:
            leftChild = 2 * i + 1
            rightChild = 2 * i + 2
            largestChild = i
            if leftChild < len(self.heap) and self.heap[leftChild] > self.heap[largestChild]:
                largestChild = leftChild
            if rightChild < len(self.heap) and self.heap[rightChild] > self.heap[largestChild]:
                largestChild = rightChild
            if largestChild == i:
                break
            temp = self.heap[i]
            self.heap[i] = self.heap[largestChild]
            self.heap[largestChild] = temp
            i = largestChild

    def buildHeap(self, A):
        self.heap = A
        for i in range(len(A)//2, -1, -1):
            self.heapify(i)

    def pop(self):
        res = self.heap[0]
        self.heap = self.heap[1:]
        self.heapify(0)
        return res

heap = growing_heap()
heap.buildHeap([0, 0, 9, 5, 23, 0, 0, 2, 2, 1, 4, 0, 12, -1, 0])
print(heap)
print(heap.pop())
print(heap)
