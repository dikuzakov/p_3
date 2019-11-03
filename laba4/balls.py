from tkinter import *
from random import randrange as rnd, choice
import random
import math as m


def create_ball():
    global Aball
    for i in range(len(Aball)):
        Aball[i].delete()
    Aball.clear()
    for i in range(random.randint(1, 5)):
        Aball.append(Ball(rnd(100, 700), rnd(100, 500)))
        Aball[i].draw()
    for i in range(len(Aball)):
        Aball[i].motion()

    root.after(3000, create_ball)


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
        #gravitation
        self.t += m.pi / 150
        a = 2.5
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
        '''for i in range(len(Aball)):
            for j in range(i + 1, len(Aball)):
                Aball[i].hit(Aball[j])'''

        root.after(70, self.motion)

    def check(self, x, y):
        if (x - self.x)**2 + (y - self.y)**2 < (self.r)**2:
            return True
        else:
            return False

    def redraw(self):
        c.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    '''def hit(self, ball):
        if((self.x - ball.x)**2 + (self.y - ball.y)**2 < (self.r + ball.r)**2):
            ux = ball.dx
            uy = ball.dy
            vx = self.dx
            vy = self.dy
            alpha = m.atan((ball.y - self.y) / (ball.x - self.x))
            vx -= ux
            vy -= uy
            beta = m.atan(-vy / -vx)
            vp = m.sqrt(vy**2 + vx**2) * m.cos(alpha - beta)
            vs = m.sqrt(vy**2 + vx**2) * m.sin(alpha - beta)
            ux += vp * m.cos(alpha)
            uy += vp * m.sin(alpha)
            vx -= vp * m.cos(alpha) - vs * m.sin(beta)
            vy += vp * m.sin(alpha) - vs * m.cos(beta)
            ball.dx = ux
            ball.dy = uy
            self.dx = vx
            self.dy = vy'''


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
            c.itemconfig(MyText, text = "points = {0}".format(point))
    if deko > -1:
        Aball.remove(Aball[deko])


point = 0
root = Tk()
W = 800
H = 700
c = Canvas(root, width=W, height=H, bg='white')
c.pack()
color = ['red', 'orange', 'yellow', 'green', 'blue']
Aball = []
MyText = c.create_text(40, 40, text="", anchor=NW, font="arial 20")
create_ball()
c.bind('<Button-1>', click)
root.mainloop()

