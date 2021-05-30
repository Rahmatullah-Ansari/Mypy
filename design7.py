from turtle import *
from random import *
bgcolor("black")
speed(0)
def rot():
    for i in range(20):
        lt(i)
        fd(i+20)
        bk(i-5)
try:
    for i in range(50):
        r=randint(0,255)
        # g=randint(1,255)
        # b=randint(2,255)
        # colormode(255)
        pencolor("yellow")
        rt(60)
        fd(200)
        rot()
        fd(50)
    hideturtle()
    done()
except:
    pass