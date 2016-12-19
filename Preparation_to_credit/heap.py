import random

class growing_heap:
    A = []

    def add(self, item):
        self.A.append(item)
        self.__heapify()

    def __str__(self):
        return str(self.A)

    def __heapify(self):    # Очень сильное колдунство
        i = 1
        while 2 * i + 1 < len(self.A) and self.A[i] < max(self.A[2 * i], self.A[2 * i + 1]):    # Пока не прострелили колено + пока батя меньше своих детей (то есть, надо его вниз)
            if self.A[2 * i] > self.A[2 * i + 1]:
                self.A[i], self.A[2 * i] = self.A[2 * i], self.A[i]
                i *= 2 # Ушли ниже
            else:
                self.A[i], self.A[2 * i + 1] = self.A[2 * i + 1], self.A[i]
                i = 2 * i + 1 # Ушли уже на левого
        if 2 * i == len(self.A) - 1 and self.A[i] < self.A[2 * i]:  # Супер-костыль от Т.Ф. - отдельно рассмотреть последнюю итерацию
            self.A[i], self.A[2 * i] = self.A[2 * i], self.A[i]

    def pop(self):
        if len(self.A) == 2:
            return self.A.pop()
        tmp = self.A[1]
        self.A[1] = self.A.pop()
        self.__heapify()
        return tmp

test = growing_heap()
[test.add(random.randint(1, 100)) for x in range(100)]
print(test)
test.pop()
print(test)
