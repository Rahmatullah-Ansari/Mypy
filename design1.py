import turtle
n = turtle.Turtle()
n.pensize(2)
n.speed(10)
n.color("blue")
try:
    for i in range(181):
        n.fd(150)
        n.left(i+90)
        n.bk(-150)
        n.rt(i-30)
    n.hideturtle()
    turtle.done()
except:
    pass