#coding=utf-8
import re


class Turing:

    commands = []
    state = '1'
    data = []
    where = 0

    def __init__(self):
        self.state = str(input("Введите начальное состояние: "))
        with open('rules.txt') as f:
            for i in f.read().split('\n'):
                self.commands.extend(re.findall('^(.)q(\d+)->(.)(q(\d+)(.)|STOP)$', i))
        print(self.commands)

        with open('data.txt', 'r') as f:
            #self.data.extend('B' for x in range(20))
            self.data.extend([x for x in f.read()])
            #self.data.extend('B' for x in range(20))
        print(self.data)


# Собственно сама прогулка по строке, начинаем с левого края
    def start(self, s=1):
        for i in range(len(self.commands)):
            if self.commands[i][0] == self.data[s] and self.commands[i][1] == self.state: # Наш клиент
                self.state = self.commands[i][4]
                self.data[s] = self.commands[i][2]
                if self.commands[i][3] == 'STOP':    # Заканчиваем наше выступление
                    return
                if self.commands[i][5] == 'R':
                    self.start(s+1)
                if self.commands[i][5] == 'L':
                    self.start(s-1)
                break

t = Turing()
t.start()
print(t.data)
