from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)


class Ball:
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
        self.id = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 10

    def set_coords(self):
        canvas.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        ay = - 1.5
        if (self.y + self.r < 580):
            self.x += self.vx
            self.y += self.vy
            self.vy -= ay
        self.set_coords()

        if self.y + self.r > 580:
            self.live -= 1
            self.vx = 0.5*self.vx
            self.vy = (-0.8)*self.vy

        if self.x + self.r > 800:
            self.vx = (-0.8)*self.vx

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    f2_power = 10
    f2_on = 0
    angle = 1

    def __init__(self):
        self.id = canvas.create_line(20, 450, 50, 420, width=7)
    # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = self.f2_power * math.sin(self.angle)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, 20, 450,
                      20 + max(self.f2_power, 20) * math.cos(self.angle),
                      450 + max(self.f2_power, 20) * math.sin(self.angle)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Target:
    x = rnd(600, 750)
    y = rnd(300, 550)
    r = rnd(2, 50)
    points = 0
    live = 1

    def __init__(self):
        self.id = canvas.create_oval(0, 0, 0, 0)
        self.id_points = canvas.create_text(30, 30, text = self.points, font ='28')
        self.new_target()
    # FIXME: don't work!!! How to call this functions when object is created?

    def new_target(self):
        """ Инициализация новой цели. """
        color = 'red'
        canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self):
        """Попадание шарика в цель."""
        canvas.coords(self.id, -10, -10, -10, -10)
        self.points += 1
        print('points')
        canvas.itemconfig(self.id_points, text=self.points)


t1 = Target()
screen1 = canvas.create_text(400, 300, text='', font='28')
gun = Gun()
bullet = 0
balls = []


def new_game():
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canvas.bind('<Button-1>', gun.fire2_start)
    canvas.bind('<ButtonRelease-1>', gun.fire2_end)
    canvas.bind('<Motion>', gun.targetting)

    t1.live = 1
    while t1.live or balls:
        for b in balls:
            if b.live == 0:
                canvas.delete(b.id)
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canvas.bind('<Button-1>', '')
                canvas.bind('<ButtonRelease-1>', '')
                canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canvas.update()
        time.sleep(0.03)
        gun.targetting()
        gun.power_up()
    canvas.itemconfig(screen1, text='')
    canvas.delete(Gun)
    root.after(50, new_game)


new_game()
root.mainloop()
