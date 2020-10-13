import turtle
import random
from turtle import *


def D(x, y):
    return x - 300, y


def pot(x, y):
    up()
    goto(D(x, y))
    dot(3, "black")
    ht()


def line(x0, y0, x1, y1):
    up()
    goto(D(x0, y0))
    down()
    goto(D(x1, y1))
    up()
    ht()


def figurexy(x0: float, y0: float, x1: float, y1: float, t: float):
    s = x1 - x0
    k = (y1 - y0) / (x1 - x0)
    b = y1 - k * x1
    xt = s * t + x0
    yt = k * xt + b
    return xt, yt


delay(0)
bgcolor("black")
color("black")
screensize(400, 400)
x0 = 0
y0 = 0
x1 = 20
y1 = -200
x2 = 650
y2 = 300

line(x0, y0, x1, y1)
line(x1, y1, x2, y2)
up()
goto(-300, 0)
ht()

print(figurexy(200, 200, 400, 0, 0.1))

for i in range(100):
    if (i % 2 == 0) is True:
        continue
    xt0, yt0 = figurexy(x0, y0, x1, y1, (i + 1) / 100)
    xt1, yt1 = figurexy(x1, y1, x2, y2, (i + 1) / 100)
    # pot(xt0, yt0)
    # pot(xt1, yt1)
    line(xt0, yt0, xt1, yt1)
    xt2, yt2 = figurexy(xt0, yt0, xt1, yt1, (i + 1) / 100)
    down()
    r = hex(random.randint(16, 255))
    g = hex(random.randint(16, 255))
    b = hex(random.randint(16, 255))
    rgb = r[2:] + g[2:] + b[2:]
    pencolor('#' + rgb)
    goto(D(xt2, yt2))
    up()
    # print(xt2, yt2)
    #pot(xt2, yt2)


done()
