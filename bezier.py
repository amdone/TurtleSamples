import turtle
import random
from turtle import *

pencolor("red")
def D(x, y):
    return x - 300, y


def pot(x, y):
    up()
    goto(D(x, y))
    dot(3, "red")
    ht()


def line(x0, y0, x1, y1):
    up()
    goto(D(x0, y0))
    down()
    goto(D(x1, y1))
    up()
    ht()


def randrgb():
    r = hex(random.randint(16, 255))
    g = hex(random.randint(16, 255))
    b = hex(random.randint(16, 255))
    rgb = '#' + r[2:] + g[2:] + b[2:]
    return rgb


def figurexy(x0: float, y0: float, x1: float, y1: float, t: float):
    s = x1 - x0
    if s == 0:
        return x0, y0 + (y1 - y0) * t
    k = (y1 - y0) / s
    b = y1 - k * x1
    xt = s * t + x0
    yt = k * xt + b
    return xt, yt


delay(1)
bgcolor("black")
color("red")
screensize(400, 400)
x0 = 0
y0 = 0
x1 = 200
y1 = 30
x2 = 0
y2 = 200
x3 = 200
y3 = 230


line(x0, y0, x1, y1)
# line(x1, y1, x2, y2)
line(x2, y2, x3, y3)
up()
goto(-300, 0)
ht()

print(figurexy(200, 200, 400, 0, 0.1))

for i in range(100):
    if (i % 2 == 0) is True:
        pass
    xt0, yt0 = figurexy(x0, y0, x1, y1, (i + 1) / 100)
    xt1, yt1 = figurexy(x1, y1, x2, y2, (i + 1) / 100)
    xt2, yt2 = figurexy(x2, y2, x3, y3, (i + 1) / 100)
    # pot(xt0, yt0)
    # pot(xt1, yt1)
    #line(xt0, yt0, xt1, yt1)
    xt4, yt4 = figurexy(xt0, yt0, xt1, yt1, (i + 1) / 100)
    xt5, yt5 = figurexy(xt1, yt1, xt2, yt2, (i + 1) / 100)
    xt6, yt6 = figurexy(xt4, yt4, xt5, yt5, (i + 1) / 100)
    down()
    pencolor("red")
    line(xt4,yt4,xt5,yt5)
    goto(D(xt6, yt6))
    up()
    # print(xt2, yt2)
    #line(xt2, yt2)


done()
