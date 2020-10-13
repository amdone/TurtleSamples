import turtle
import random
import time
from turtle import *

pencolor("red")
def D(x, y):
    return x - 400, y


def pot(x, y):
    up()
    goto(D(x, y))
    write('.')
    ht()


def line(x0, y0, x1, y1):
    up()
    goto(D(x0, y0))
    down()
    goto(D(x1, y1))
    up()
    goto(D(0, 0))
    ht()


def randrgb():
    r = hex(random.randint(16, 255))
    g = hex(random.randint(16, 255))
    b = hex(random.randint(16, 255))
    rgb = '#' + r[2:] + g[2:] + b[2:]
    return rgb


def figurexy(x0: float, y0: float, x1: float, y1: float, t: float):
    line(x0,y0,x1,y1)
    s = x1 - x0
    if s == 0:
        return x0, y0 + (y1 - y0) * t
    k = (y1 - y0) / s
    b = y1 - k * x1
    xt = s * t + x0
    yt = k * xt + b
    #pot(xt,yt)
    return xt, yt
    
    
def l2p(l: list, t: float):
	if len(l) == 2:
		xt, yt = figurexy(l[0][0], l[0][1], l[1][0], l[1][1], t)
		pencolor('blue')
		line(l[0][0], l[0][1], l[1][0], l[1][1])
		pot(xt, yt)
		pencolor('blue')
		return xt, yt
	else:
		nl = []
		for i in range(len(l)-1):
			x, y = figurexy(l[i][0], l[i][1], l[i+1][0], l[i+1][1], t)
			#line(l[i][0], l[i][1], l[i+1][0], l[i+1][1])
			#pot(x,y)
			nl.append([x, y])
	return l2p(nl, t)


def draw(plist: list, r):
	drawLine = True
	if drawLine is True:
		down()
		for i in plist:
			goto(D(i[0], i[1]))
	#line(x0, y0, x1, y1)
	#line(x1, y1, x2, y2)
	#line(x2, y2, x3, y3)
	up()
	goto(-400, 0)
	ht()
	down()
	pencolor('blue')
	for t in range(0, 10001, r*1):
		tracer(False)
		clear()
		x, y = l2p(plist, t*0.0001)
		pencolor('red')
		goto(D(x,y))
		ontimer(ht(),2)
		tracer(True)
	#goto(D(plist[len(plist)-1][0],plist[len(plist)-1][1]))
	up()
	goto(D(0, 0))
	ht()
	
ht()
#delay(2)
tracer(False)
#speed(0)
bgcolor("white")
color("red")
screensize(400, 400)

pi=[[0,0],
		[400,400],
		[800,0]
]
pi2 = [[0, 0],
		[400, 0],
		[800, 200],
		[900, 600],
		[500,800],
		[100,600],
		[300,200]
		]

up()
goto(-400, 0)
ht()
time.sleep(0)

#print(figurexy(200, 200, 400, 0, 0.1))

#right(90)
#pensize(10)
#write(time.clock_gettime(0))
draw(pi2,10)
right(90)
fd(100)
#write(time.clock_gettime(0))

	#clear()
done()
	
	
draw(pi,50)

#for i in range(0, 100, 1):
	


done()
