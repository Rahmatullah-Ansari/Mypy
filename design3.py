import math
import turtle
wn=turtle.Screen()
wn.bgcolor("skyblue")
tk=turtle.Turtle()
tk.pensize(3)
tk.color("red")
tk.shape("arrow")
tk.speed(0)
try:
    for i in range(1,47):
        tk.fd(50+i)
        tk.lt(70)
        tk.bk(150)
        tk.circle(8)
    tk.hideturtle()
    turtle.done()
except:
     pass