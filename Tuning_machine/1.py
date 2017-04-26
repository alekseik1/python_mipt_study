# coding=utf-8

import re


class Turing:
    commands = []
    state = '1'
    data = []
    finish = False

    def __init__(self, rules='rules.txt'):
        self.state = str(input("Введите начальное состояние: "))
        with open(rules) as f:
            for i in f.read().split('\n'):
                self.commands.extend(re.findall('^(.)q(\d+)->(.)(q(\d+)(.)|STOP)$', i))
        # print(self.commands)

        with open('data.txt', 'r') as f:
            self.data.extend('B')
            self.data.extend([x for x in f.read()])
            self.data.extend('B')
            # print(self.data)


        # Собственно сама прогулка по строке, начинаем с левого края

    def start(self, s=1):
        for i in range(len(self.commands)):
            if self.commands[i][0] == self.data[s] and self.commands[i][1] == self.state:  # Наш клиент
                self.state = self.commands[i][4]
                self.data[s] = self.commands[i][2]
                if self.commands[i][3] == 'STOP':  # Заканчиваем наше выступление
                    self.finish = True
                    return 0
                if self.commands[i][5] == 'R':
                    return 1
                if self.commands[i][5] == 'L':
                    return -1
                break

    def calc(self):
        where = 1
        while True:
            a = self.start(where)
            if a == 1:
                where += 1
            elif a == -1:
                where -= 1
            else:
                break
        return self

    def print(self):
        print(*self.data)


mult = Turing('mult2.txt')
mult.calc().print()

