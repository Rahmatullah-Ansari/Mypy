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
     for i in range(1,301):
          tk.fd(5)
          tk.penup()
          tk.fd(10)
          tk.pd()
          tk.fd(i+10)
          tk.rt(70)
     # tk.end_fill()
     tk.hideturtle()
     turtle.done()
except:
     pass