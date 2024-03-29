from random import randrange as rnd, choice
import tkinter as tk
import math
import time


class Scoreboard:
    global canvas

    def __init__(self):
        self.score = 0
        self.id_points = canvas.create_text(30, 30, text=self.score, font='28')

    def update_score(self, point=1):
        self.score += point
        canvas.itemconfig(self.id_points, text=self.score)


class Shell:
    global gun

    def __init__(self):
        self.time = 0
        self.wall = 10
        self.x = gun.x + max(gun.f2_power, 20) * math.cos(gun.angle)
        self.y = gun.y + max(gun.f2_power, 20) * math.sin(gun.angle)
        self.r = rnd(7, 10)
        self.ay = 1.5
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])

    def hittest(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            return True
        else:
            return False

    def move(self):
        if self.y + self.r < 600 and self.x + self.r < 800:
            self.time += 1
            self.x += self.vx
            self.y -= self.vy
            self.vy -= self.ay

        elif self.y + self.r > 600:
            self.wall -= 1
            self.vx = 0.6*self.vx

            self.vy = (-0.6)*self.vy
            self.y = 599 - self.r

        elif self.x + self.r > 800:
            self.wall -= 1
            self.vx = (-0.6)*self.vx
            self.x = 799 - self.r
        if abs(self.vy) < 5 and self.y + self.r >= 600 + self.vy:
            self.y = 600 - self.r
            self.vy = 0
            self.wall -= 1
        self.draw()

    def draw(self):
        pass


class Ball(Shell):
    global gun

    def __init__(self):
        Shell.__init__(self)
        self.id = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )

    def draw(self):
        canvas.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )


class Rectangle(Shell):
    global gun

    def __init__(self):
        Shell.__init__(self)
        self.n = rnd(3, 10)
        self.points = []
        for i in range(self.n):
            self.points += (self.x + self.r * math.cos(math.pi * 2 * i / self.n), self.y - self.r * math.sin(math.pi * 2 * i / self.n))
        self.id = canvas.create_polygon(self.points, outline="black")
        canvas.itemconfig(self.id, fill=self.color)

    def draw(self):
        self.points = []
        for i in range(self.n):
            self.points += (self.x + self.r * math.cos(math.pi * 2 * i / self.n), self.y - self.r * math.sin(math.pi * 2 * i / self.n))
        canvas.coords(
            self.id,
            self.points
        )


class Gun:

    def __init__(self):
        global canvas
        self.f2_power = 10
        self.f2_on = 0
        self.angle = 1
        self.x = 20
        self.y = 450
        self.id = canvas.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Rectangle()
        new_ball.r += 5
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = - self.f2_power * math.sin(self.angle)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, self.x, self.y,
                      self.x + max(self.f2_power, 20) * math.cos(self.angle),
                      self.y + max(self.f2_power, 20) * math.sin(self.angle)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')

    def move(self, x, y):
        self.x += x
        self.y += y


class Target:
    def __init__(self):
        self.x = rnd(500, 750)
        self.y = rnd(300, 500)
        self.r = rnd(20, 40)
        self.vx = 0
        self.vy = rnd(-5, 5)
        self.ay = 0
        self.color = 'red'
        self.live = 1

    def hit(self):
        canvas.coords(self.id, -10, -10, -10, -10)

    def draw(self):
        pass

    def move(self):
        if self.y - self.r < 0:
            self.y = self.r + 1
            self.vy = (-1) * self.vy
        elif self.y + self.r > 600:
            self.y = 600 - self.r - 1
            self.vy = (-1) * self.vy
        else:
            self.y -= self.vy
        self.draw()

    def hittest(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            return True
        else:
            return False


class TargetBall(Target):

    def __init__(self):
        Target.__init__(self)
        self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canvas.itemconfig(self.id, fill=self.color)

    def draw(self):
        canvas.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )


class TargetRectangle(Target):
    def __init__(self):
        Target.__init__(self)
        self.n = rnd(3, 10)
        self.points = []
        for i in range(self.n):
            self.points += (self.x + self.r * math.cos(math.pi * 2 * i / self.n), self.y - self.r * math.sin(math.pi * 2 * i / self.n))
        self.id = canvas.create_polygon(self.points, outline="black")
        canvas.itemconfig(self.id, fill=self.color)

    def draw(self):
        self.points = []
        for i in range(self.n):
            self.points += (self.x + self.r * math.cos(math.pi * 2 * i / self.n), self.y - self.r * math.sin(math.pi * 2 * i / self.n))
        canvas.coords(
            self.id,
            self.points
        )


def new_game():
    global balls, bullet, score, target_number, to_del, i
    bullet = 0
    balls = []
    targets = []
    targets_lives = 0
    targets.append(TargetBall())
    targets.append(TargetRectangle())
    for i in range(target_number):
        targets_lives += targets[i].live

    canvas.bind('<Button-1>', gun.fire2_start)
    canvas.bind('<ButtonRelease-1>', gun.fire2_end)
    canvas.bind('<Motion>', gun.targetting)
    root.bind('<Up>', lambda event: gun.move(0, -2))
    root.bind('<Down>', lambda event: gun.move(0, 2))
    root.bind('<Left>', lambda event: gun.move(-2, 0))
    root.bind('<Right>', lambda event: gun.move(2, 0))
    canvas.itemconfig(screen1, text='')
    while targets_lives:
        to_del = []
        for j in range(target_number):
            if targets[j].live == 1:
                targets[j].move()

        for i, b in enumerate(balls):
            if b.wall == 0:
                to_del.append(i)
                canvas.delete(b.id)
            if b.time >= 20 and b.time <= 500:
                two_figure(b)
            else:
                b.move()
            for j in range(target_number):
                if b.hittest(targets[j]) and targets[j].live:
                    targets_lives -= targets[j].live
                    targets[j].live = 0
                    targets[j].hit()
                    score.update_score()

        if to_del:
            for i in range(len(to_del) - 1, -1, -1):
                del balls[to_del[i]]

        canvas.update()
        time.sleep(0.03)
        gun.targetting()
        gun.power_up()
    for i in range(len(balls) - 1, -1, -1):
            canvas.delete(balls[i].id)
            del balls[i]
    del targets
    canvas.bind('<Button-1>', '')
    canvas.bind('<ButtonRelease-1>', '')
    canvas.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
    time.sleep(0.03)
    canvas.delete(gun)
    root.after(1000, new_game)

def two_figure(b):
    global balls, to_del, i
    print(to_del)
    new_ball_1 = Rectangle()
    new_ball_1.x = b.x
    new_ball_1.y = b.y
    new_ball_1.vx = b.vx + rnd(-5, 5)
    new_ball_1.vy = b.vy + rnd(-5, 5)
    new_ball_1.draw()
    new_ball_2 = Rectangle()
    new_ball_2.x = b.x
    new_ball_2.y = b.y
    rd = 10
    new_ball_2.vx = b.vx + rnd(-rd, rd)
    new_ball_2.vy = b.vy + rnd(-rd, rd)
    new_ball_2.draw()
    new_ball_1.time = 2000
    new_ball_2.time = 2000
    canvas.delete(b.id)
    to_del.append(i)
    b.x = -10
    b.y = -10
    b.vx = 0
    b.vy = 0
    b.time = 2000
    balls += [new_ball_1]
    balls += [new_ball_2]

def main():
    global root, canvas, screen1, gun, bullet, balls, score, target_number
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    screen1 = canvas.create_text(400, 300, text='', font='28')
    gun = Gun()
    bullet = 0
    balls = []
    score = Scoreboard()
    target_number = 2


main()
new_game()
tk.mainloop()
