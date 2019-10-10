from tkinter import *
from random import randrange as rnd, choice
import time

cl = ['red','orange','yellow','green','blue']

e = Entry(root, width=20)
b = Button(root, text = "Очки")
l = Label(root, bg='black', fg='white', width=20)

def create_ball():
    c.delete(ALL)
    ball = Ball(rnd(100,700), rnd(100,500))
    ball.draw()
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
        c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = choice(cl))

root = Tk()
c = Canvas(root, width = 800, height = 800, bg = 'white')
c.pack()

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
