from random import randrange as rnd, choice
from tkinter import *
import math

# print (dir(math))

import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class ball():
    """ Класс ball описывает мяч. """

    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.live = 30

    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        """ Метод move описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения 
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
        """
        # Чет работает
        self.x += self.vx
        self.y -= self.vy
        self.ballx = t1.x
        self.bally = t1.y
        self.ball2x = t2.x
        self.ball2y = t2.y
        r = 25
        if t1.live:
            self.ballx += self.vx*0.2
            self.bally -= self.vy*0.1
            t1.update_coord(self.ballx + rnd(-r, r), self.bally + rnd(-r, r), t1.r)
        if t2.live:
            self.ball2x -= self.vx*(-0.05)
            self.ball2y += self.vy*0.1
            t2.update_coord(self.ball2x + rnd(-r, r), self.ball2y + rnd(-r, r), t2.r)
        self.vy -= 5 + 0.03*self.vy
        if self.x >= 800:
            self.vx = -self.vx
        if self.x <= 0:
            self.vx = -self.vx
        if self.y <= 0:
            self.vy = -self.vy
        if self.y >= 600:
            self.vy = -self.vy
        self.set_coords()
        #if abs(self.x-t1.r) == self.x and abs(self.y - ob.r) == self.y:



    def hittest(self, ob):
        """ Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте ob.

        Args:
            ob: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x >= ob.x-ob.r and self.x <= ob.x+ob.r) and (self.y >= ob.y - ob.r and self.y <= ob.y + ob.r):
            return True
        return False


class gun():
    """ Класс gun описывает пушку. """

    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1

        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """ Выстрел мячом происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """ Прицеливание. Зависит от положения мыши.
        """
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target1():
    """ Класс target описывает цель. """
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def update_coord(self, x, y, r):
        canv.coords(self.id, x - r, y - r, x + r, y + r)
    def get_coord(self):
        return [self.x, self.y]

    def hit(self, points=1):
        """ Попадание шарика в цель. """

        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = target1()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []

class target2():
    """ Класс target описывает цель. """
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def update_coord(self, x, y, r):
        canv.coords(self.id, x - r, y - r, x + r, y + r)

    def get_coord(self):
        return [self.x, self.y]

    def hit(self, points=1):
        """ Попадание шарика в цель. """

        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t2 = target2()

def new_game(event=''):
    global gun, t1, screen1, balls, bullet, t2, hit
    hit = 0
    t1.new_target()
    t2.new_target()
    try:
        canv.itemconfig(screen1, text='')
    except:
        print('')
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live and t2.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                hit += 1
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                hit += 1
            if hit == 2:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                canv.delete(gun)
                canv.update()
                root.after(750, new_game)
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)

new_game()
mainloop()
