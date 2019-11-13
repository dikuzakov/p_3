from tkinter import *
from random import randrange as rnd, choice
import random
import math as m


def new_game():
    global miss, c
    c.itemconfig(MyText, text="Не делайте больше пяти промахов!")
    create_ball()


def end_game():
    global btn, c
    for i in range(len(Aball)):
        Aball[i].delete()
    Aball.clear()


def restart(event):
    global miss, c, point
    miss = 0
    point = 0
    score_label['text'] = 'Ваши очки:' + str(point)
    new_game()


def cancel():
    global job
    root.after_cancel(job)
    job = None
    end_game()


def create_ball():
    global Aball, job
    for i in range(len(Aball)):
        Aball[i].delete()
    Aball.clear()
    for i in range(random.randint(5, 10)):
        Aball.append(Ball(rnd(100, 700), rnd(100, 500)))
        Aball[i].draw()
    for i in range(len(Aball)):
        Aball[i].motion()
    job = root.after(7000, create_ball)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def lambdamultiplication(self, l):
        self.x *= l
        self.y *= l
        return self

    def __add__(self, other):
        vector = Vector(self.x + other.x, self.y + other.y)
        return vector

    def __sub__(self, other):
        vector = Vector(self.x - other.x, self.y - other.y)
        return vector

    def __neg__(self):
        vector = Vector(- self.x, - self.y)
        return vector

    def __abs__(self):
        return m.sqrt(self.x ** 2 + self.y ** 2)

    def pr(self, other):
        return other.lambdamultiplication(other.__mul__(self) / (other.__abs__() ** 2))


class Ball:
    r_min = 20
    r_max = 50
    t = 0

    def __init__(self, x_coord, y_coord):
        self.r = rnd(self.r_min, self.r_max)
        self.x = x_coord
        self.y = y_coord
        speed = 15
        self.dx = 0.5 * (rnd(-speed, speed) + rnd(-speed, speed))
        self.dy = 0.5 * (rnd(-speed, speed) + rnd(-speed, speed))
        self.id = 0

    def draw(self):
        self.id = c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=choice(color))

    def delete(self):
        c.delete(self.id)

    def motion(self):
        # gravitation
        self.t += m.pi / 150
        a = 0.5
        ay = a * m.cos(self.t % 2 * m.pi)
        ax = a * m.sin(self.t % 2 * m.pi)
        global c, Aball
        if self.x + self.r > W:
            self.dx = (-1) * self.dx
            self.x = W - self.r
        elif self.x - self.r < 0:
            self.dx = (-1) * self.dx
            self.x = self.r
        elif self.y + self.r > H - 100:
            self.dy = (-1) * self.dy
            self.y = H - 100 - self.r
        elif self.y - self.r < 0:
            self.dy = (-1) * self.dy
            self.y = self.r

        self.dy += ay
        self.dx += ax
        self.x += self.dx
        self.y += self.dy
        self.redraw()
        for i in range(len(Aball)):
            for j in range(i + 1, len(Aball)):
                Aball[i].hit(Aball[j])
        root.after(70, self.motion)

    def check(self, x, y):
        if (x - self.x) ** 2 + (y - self.y) ** 2 < (self.r) ** 2:
            return True
        else:
            return False

    def redraw(self):
        c.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def hit(self, ball):
        # иногда шарики меняются координатами - не понимаю, почему
        if ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2 < (self.r + ball.r) ** 2):
            v1 = Vector(self.dx, self.dy)
            v2 = Vector(ball.dx, ball.dy)
            r = Vector(ball.x - self.x, ball.y - self.y)
            dr = r.lambdamultiplication(-(m.sqrt((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) + (self.r + ball.r)) / abs(r))
            #p - скорость вдоль r, s - скорость перпендикулярная
            v1p = v1.pr(r)
            v1s = v1 - v1p
            v2p = v2.pr(-r)
            v2s = v2 - v2p
            (v1p, v2p) = (v2p, v1p)
            v1 = v1p + v1s
            v2 = v2p + v2s
            self.dx = v1.x
            self.dy = v1.y
            ball.dx = v2.x
            ball.dy = v2.y
            ball.x += dr.x / 2
            ball.y += dr.y / 2
            self.x -= dr.x / 2
            self.y -= dr.y / 2


def click(event):
    global point, MyText, c, miss
    if miss >= 4:
        cancel()

    deko = -1
    for i in range(len(Aball)):
        if Aball[i].check(event.x, event.y):
            Aball[i].delete()
            point += 1
            deko = i
            score_label['text'] = 'Ваши очки:' + str(point)
    if deko > -1:
        Aball.remove(Aball[deko])
    else:
        miss += 1
        c.itemconfig(MyText, text="miss = {0}".format(miss))


miss = 0
job = None
point = 0
root = Tk()
W = 800
H = 700
root.geometry(str(W) + 'x' + str(H))
c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)
color = ['red', 'orange', 'yellow', 'green', 'blue']
Aball = []
MyText = c.create_text(40, 40, text="", anchor=NW, font="arial 20")
score_label = Label(root, bg='black', fg='white', width=20)
score_label.pack(anchor=NE)
btn = Button(root, text="Start/Restart")
btn.pack(anchor=NE)
new_game()
c.bind('<Button-1>', click)
btn.bind('<Button-1>', restart)
root.mainloop()
