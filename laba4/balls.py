from tkinter import *
from random import randrange as rnd, choice
import random
import math as m

'''def create_ball():
    global Aball
    for i in range(len(Aball)):
        Aball[i].delete()
    Aball.clear()
    for i in range(random.randint(1, 5)):
        Aball.append(Ball(rnd(100, 700), rnd(100, 500)))
        Aball[i].draw()
    for i in range(len(Aball)):
        Aball[i].motion()

    root.after(3000, create_ball)'''


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def lmul(self, l):
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
        return other.lmul(other.__mul__(self) / (other.__abs__() ** 2))


class Ball:
    r_min = 20
    r_max = 50
    t = 0

    def __init__(self, x_coord, y_coord):
        self.r = rnd(self.r_min, self.r_max)
        self.x = x_coord
        self.y = y_coord
        speed = 30
        self.dx = rnd(-speed, speed)
        self.dy = rnd(-speed, speed)
        self.id = 0

    def draw(self):
        self.id = c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=choice(color))

    def delete(self):
        c.delete(self.id)

    def motion(self):
        # gravitation
        self.t += m.pi / 150
        a = 0
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
        if ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2 < (self.r + ball.r) ** 2):
            v1 = Vector(self.dx, self.dy)
            v2 = Vector(ball.dx, ball.dy)
            r = Vector(ball.x - self.x, ball.y - self.y)
            v1p = v1.pr(r)
            v1s = v1 - v1p
            print(v1p.x, v1p.y)
            v2p = v2.pr(r)
            print(v1p.x, v1p.y)
            v2s = v2 - v2p
            (v1p, v2p) = (v2p, v1p)
            v1 = v1p + v1s
            v2 = v2p + v2s
            self.dx = v1.x
            self.dy = v1.y
            ball.dx = v2.x
            ball.dy = v2.y


def click(event):
    global point
    global MyText
    global c
    deko = -1
    print("Click!")
    for i in range(len(Aball)):
        if Aball[i].check(event.x, event.y):
            Aball[i].delete()
            point += 1
            deko = i
            print(point)
            c.itemconfig(MyText, text="points = {0}".format(point))
    if deko > -1:
        Aball.remove(Aball[deko])


v1 = Vector(20, 0)
v2 = Vector(10, 0)
v = Vector(10, 0)
#print(v2.x, v2.y)
#print(v1.x, v1.y)
v1r = v1.pr(v)
#print(v1.x, v1.y)
#print(v2.x, v2.y)
vec1 = Vector(1, 0)
vec2 = Vector(2, 0)
#print(vec1.pr(vec2).x, vec1.pr(vec2).y)
point = 0
root = Tk()
W = 800
H = 700
c = Canvas(root, width=W, height=H, bg='white')
c.pack()
color = ['red', 'orange', 'yellow', 'green', 'blue']
Aball = []
MyText = c.create_text(40, 40, text="", anchor=NW, font="arial 20")

ball1 = Ball(100, 50)
ball1.dx = 10
ball1.dy = 0
ball2 = Ball(700, 50)
ball2.dx = - 10
ball2.dy = 0
ball1.draw()
ball2.draw()
ball1.motion()
ball2.motion()
Aball.append(ball1)
Aball.append(ball2)
# create_ball()
c.bind('<Button-1>', click)
root.mainloop()
