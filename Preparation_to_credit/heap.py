class growing_heap:
    A = []

    def add(self, item):
        self.A.append(item)
        i = len(self.A) - 1
        while i > 1 and self.A[i//2] < item:    # Пока батя меньше своего пез... эээ, дочернего элемента
            self.A[i] = self.A[i//2]
            i //= 2
            self.A[i] = item

    def pop(self):
        if len(self.A) == 2:
            return self.A.pop()
        tmp = self.A[1]
        self.A[1] = self.A.pop()
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
        return tmp
