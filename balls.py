from tkinter import *
from random import randrange as rnd, choice
import time \
 \
 \
def create_ball():
    ball = Ball(rnd(100, 700), rnd(100, 500))
    ball.draw()
    c.tag_bind(ball.id, '<Button-1>', ball.delete)
    root.after(1000, create_ball)


class Object:

    def __init__(self):
        pass

    def draw(self):
        pass


class Figure(Object):

    def __init__(self, color):
        pass


class Ball(Figure):

    def __init__(self, x_coord, y_coord):
        self.r = rnd(20, 50)
        self.x = x_coord
        self.y = y_coord

    def draw(self):
        self.id = c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=choice(cl))

    def delete(self):
        c.delete(self)


root = Tk()
c = Canvas(root, width=800, height=700, bg='white')
c.pack()

cl = ['red', 'orange', 'yellow', 'green', 'blue']

oval = c.create_oval(30, 10, 130, 80, fill="orange")


def oval_func(event):
    c.delete(oval)
    c.create_text(80, 50, text="Круг")


c.tag_bind(oval, '<Button-1>', oval_func)

create_ball()
root.mainloop()
"""colors = 
def new_ball():
    canv.delete(ALL)
    x = )
    y = 
    r = rnd(30,50)
    
    root.after(1000,new_ball)


def click(event):
    print('click')

new_ball()
canv.bind('<Button-1>', click)
mainloop()"""
