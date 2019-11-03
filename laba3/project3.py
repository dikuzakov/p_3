import graph

c = graph.canvas()


def update():
    for i in obj1:
        graph.moveObjectBy(i, 5, 0)
    for j in obj2:
        graph.moveObjectBy(j, 5, 0)
    if graph.xCoord(obj1[0]) >= 1000:
        for i in obj1:
            graph.moveObjectBy(i, -1100, 0)
    if graph.xCoord(obj2[0]) >= 1000:
        for i in obj2:
            graph.moveObjectBy(i, -1100, 0)


def keyPressed(event):
    if event.keycode == VK_ESCAPE:
        graph.close()


def background(h, d):
    graph.penColor('#000000')
    graph.brushColor('#a1f5ff')
    graph.rectangle(0, 0, d, 7 / 15 * h)
    graph.brushColor('#4423df')
    graph.rectangle(0, 7 / 15 * h, d, 10 / 15 * h)
    graph.brushColor('#eef60c')
    graph.rectangle(0, 10 / 15 * h, d, h)


def clouds(x, y, s):
    # s - size's cloud
    b_c = 21 * s  # between_clouds
    r_c = 30 * s  # radius of cloud
    graph.brushColor('#ffffff')
    graph.circle(x, y, r_c)
    graph.circle(x + b_c, y + b_c, r_c)
    graph.circle(x + 2 * b_c, y, r_c)
    graph.circle(x + 3 * b_c, y + b_c, r_c)
    graph.circle(x + 4 * b_c, y, r_c)


def Sun(x, y, r_s):
    # r_s - radius of sun
    graph.penColor('#fff71d')
    graph.brushColor('#fff71d')
    graph.circle(x, y, r_s)


def umbrella(x, y, s):
    graph.penColor('#e38219')
    graph.brushColor('#e38219')
    d_stolbik = 0.01 * d * s
    h_stolbik = 0.43 * h * s
    d_zont = 3 / 24 * d * s
    h_zont = 3 / 49 * h * s
    graph.rectangle(x, y, x + d_stolbik, y + h_stolbik)
    graph.penColor('#f45151')
    graph.brushColor('#f45151')
    graph.polygon([(x, y), (x - d_zont, y + h_zont), (x, y + h_zont), (x, y)])
    graph.rectangle(x, y, x + d_stolbik, y + h_zont)
    graph.polygon([(x + d_stolbik, y), (x + d_stolbik + d_zont, y + h_zont),
                   (x + d_stolbik, y + h_zont), (x + d_stolbik, y)])
    graph.penColor('#000000')
    graph.line(x, y, x - 0.1 * d_zont, y + h_zont)
    graph.line(x, y, x - 0.4 * d_zont, y + h_zont)
    graph.line(x, y, x - 0.7 * d_zont, y + h_zont)
    graph.line(x + d_stolbik, y, x + d_stolbik + 0.1 * d_zont, y + h_zont)
    graph.line(x + d_stolbik, y, x + d_stolbik + 0.4 * d_zont, y + h_zont)
    graph.line(x + d_stolbik, y, x + d_stolbik + 0.7 * d_zont, y + h_zont)


def ship(x, y, s):
    a = []
    r = 1 / 30 * d * s
    h_m = 0.005 * d * s
    a.append(
        c.create_arc(
            x - r,
            y - r,
            x + r,
            y + r,
            start=180,
            extent=90,
            fill='#ba5005'))
    graph.penColor('#000000')
    graph.brushColor('#ba5005')
    a.append(graph.rectangle(x, y, x + 4 * r, y + r))
    a.append(graph.polygon([(x + 4 * r, y), (x + 6 * r, y),
                            (x + 4 * r, y + r), (x + 4 * r, y)]))
    graph.brushColor('#000000')
    a.append(graph.rectangle(x + 1.5 * r, y, x + 1.5 * r + h_m, y - 3 * r))
    graph.brushColor('#ded599')
    a.append(graph.polygon([(x +
                             1.5 *
                             r +
                             h_m, y -
                             3 *
                             r), (x +
                                  2 *
                                  r +
                                  h_m, y -
                                  1.5 *
                                  r), (x +
                                       3 *
                                       r +
                                       h_m, y -
                                       1.5 *
                                       r), (x +
                                            1.5 *
                                            r +
                                            h_m, y -
                                            3 *
                                            r)]))
    a.append(graph.polygon([(x +
                             1.5 *
                             r +
                             h_m, y), (x +
                                       2 *
                                       r +
                                       h_m, y -
                                       1.5 *
                                       r), (x +
                                            3 *
                                            r +
                                            h_m, y -
                                            1.5 *
                                            r), (x +
                                                 1.5 *
                                                 r +
                                                 h_m, y)]))
    graph.brushColor('#000000')
    a.append(graph.circle(x + 13 / 3 * r, y + 1 / 3 * r, 1 / 4 * r))
    graph.brushColor('#ffffff')
    a.append(graph.circle(x + 13 / 3 * r, y + 1 / 3 * r, 1 / 5 * r))

    return a


d = 1000
h = 700
graph.windowSize(d, h)
graph.canvasSize(d, h)
background(h, d)
clouds(0.6 * d, (10 / 75) * h, 0.9)
clouds(0.38 * d, (7 / 75) * h, 0.7)
clouds(0.1 * d, (13 / 75) * h, 1.2)
Sun(d - 0.123 * d, 0.167 * d, 50)

obj1 = ship(3.8 / 5 * d, 8 / 15 * h, 1)
obj2 = ship(3.5 / 7 * d, 8.5 / 15 * h, 0.7)
umbrella(0.25 * d, 0.55 * h, 1)
umbrella(0.50 * d, 0.65 * h, 0.7)

graph.onKey(keyPressed)
graph.onTimer(update, 50)
graph.run()
