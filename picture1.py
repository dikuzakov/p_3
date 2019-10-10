from tkinter import *
from graph import *

c = canvas()

def update():
	for i in obj1:
		moveObjectBy(i, 5, 0)
	for j in obj2:	
		moveObjectBy(j, 5, 0)
	if xCoord(obj1[0]) >= 1000:
		for i in obj1:
		    moveObjectBy(i, -1100, 0)
	if xCoord(obj2[0]) >= 1000:
		for i in obj2:
		    moveObjectBy(i, -1100, 0)
	
	
def keyPressed(event):
	if event.keycode == VK_ESCAPE:
		close()

def background(h, d):
    penColor('#000000')
    brushColor('#a1f5ff')
    rectangle(0, 0, d, 7 / 15 * h)
    brushColor('#4423df')
    rectangle(0, 7 / 15 * h, d, 10 / 15 * h)
    brushColor('#eef60c')
    rectangle(0, 10 / 15 * h, d, h)

def clouds(x, y, s):
    # s - size's cloud
    b_c = 21 * s #between_clouds
    r_c = 30 * s #radius of cloud
    brushColor('#ffffff')
    circle(x, y, r_c)
    circle(x + b_c, y + b_c, r_c)
    circle(x + 2 * b_c, y, r_c)
    circle(x + 3 * b_c, y + b_c, r_c)
    circle(x + 4 * b_c, y, r_c)

def Sun(x, y, r_s):
    # r_s - radius of sun
    penColor('#fff71d')
    brushColor('#fff71d')
    circle(x, y, r_s)


def umbrella(x, y, s):
    penColor('#e38219')
    brushColor('#e38219')
    d_stolbik = 0.01 * d * s
    h_stolbik = 0.43 * h * s
    d_zont = 3/24 * d * s
    h_zont = 3/49 * h * s
    rectangle(x, y, x + d_stolbik, y + h_stolbik)
    penColor('#f45151')
    brushColor('#f45151')
    polygon([(x, y), (x - d_zont, y + h_zont), (x, y + h_zont), (x, y)])
    rectangle(x, y, x + d_stolbik, y + h_zont)
    polygon([(x + d_stolbik, y), (x + d_stolbik + d_zont, y + h_zont), (x + d_stolbik, y + h_zont), (x + d_stolbik, y)])
    penColor('#000000')
    line(x, y, x - 0.1 * d_zont, y + h_zont)
    line(x, y, x - 0.4 * d_zont, y + h_zont)
    line(x, y, x - 0.7 * d_zont, y + h_zont)
    line(x + d_stolbik, y, x + d_stolbik + 0.1 * d_zont, y + h_zont)
    line(x + d_stolbik, y, x + d_stolbik + 0.4 * d_zont, y + h_zont)
    line(x + d_stolbik, y, x + d_stolbik + 0.7 * d_zont, y + h_zont)

def ship(x, y, s):
    a = []
    r = 1 / 30 * d * s
    h_m = 0.005 * d * s
    a.append(c.create_arc(x - r, y - r, x + r, y + r, start = 180, extent = 90, fill = '#ba5005'))
    penColor('#000000')
    brushColor('#ba5005')
    a.append(rectangle(x, y, x + 4 * r, y + r))
    a.append(polygon([(x + 4 * r, y), (x + 6 * r, y), (x + 4 * r, y + r), (x + 4 * r, y)]))
    brushColor('#000000')
    a.append(rectangle(x + 1.5 * r, y, x + 1.5 * r + h_m, y - 3 * r))
    brushColor('#ded599')
    a.append(polygon([(x + 1.5 * r + h_m, y - 3 * r), (x + 2 * r + h_m, y - 1.5 * r), (x + 3 * r + h_m, y - 1.5 * r), (x + 1.5 * r + h_m, y - 3 * r)]))
    a.append(polygon([(x + 1.5 * r + h_m, y), (x + 2 * r + h_m, y - 1.5 * r), (x + 3 * r + h_m, y - 1.5 * r), (x + 1.5 * r + h_m, y)]))
    brushColor('#000000')
    a.append(circle(x + 13/3 * r, y + 1/3 * r, 1/4 * r))
    brushColor('#ffffff')
    a.append(circle(x + 13/3 * r, y + 1/3 * r, 1/5 * r))
    
    return a
d = 1000
h = 700
windowSize(d, h)
canvasSize(d, h)
background(h, d)
clouds(0.6 * d, (10 / 75) * h, 0.9)
clouds( 0.38 * d, (7 / 75) * h, 0.7)
clouds(0.1 * d, (13 / 75) * h, 1.2)
Sun(d - 0.123 * d, 0.167 * d, 50)

obj1 = ship(3.8/5 * d, 8/15 * h, 1)
obj2 = ship(3.5/7 * d, 8.5/15 * h, 0.7)
for i in obj1:
	print(type(i))
for i in obj2:
	print(type(i))
umbrella(0.25 * d, 0.55 * h, 1)
umbrella(0.50 * d, 0.65 * h, 0.7)

onKey(keyPressed)
onTimer(update, 50)
run()

