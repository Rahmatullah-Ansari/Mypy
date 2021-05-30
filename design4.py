from turtle import *
from random import *
bgcolor('black')
x=1
speed(0)
shape("arrow")
pu()    
setpos(-150,70)
pd()
while x < 201:
    r=randint(0,255)
    g=randint(1,255)
    b=randint(2,255)
    colormode(255)
    pencolor(r,g,b)
    fd(x+50)
    lt(90)
    bk(200)
    rt(35)
    x += 1
hideturtle()
done()