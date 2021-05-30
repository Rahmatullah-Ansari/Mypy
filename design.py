import math
import turtle
wn=turtle.Screen()
wn.bgcolor("skyblue")
tk=turtle.Turtle()
tk.pensize(3)
tk.color("red")
tk.shape("arrow")
tk.speed(0)
tk.setpos(-50,0)
# tk.fillcolor("silver")
# tk.begin_fill()
try:
     for i in range(1,201):
          tk.fd(100)
          tk.rt(60)
          tk.bk(110+i)
     # tk.end_fill()
     tk.hideturtle()
     turtle.done()
except:
     pass