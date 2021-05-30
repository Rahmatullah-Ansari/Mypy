import matplotlib.pyplot as pt
import datetime
x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))
dx=(x2-x1)
dy=(y2-y1)
p=(2*dy-dx)
x=x1
y=y1
xp=[]
yp=[]
while x <= x2:
    if p < 0:
        xp.append(x)
        yp.append(y)
        p += 2*dy
    elif p >= 0:
        xp.append(x)
        yp.append(y)
        y += 1
        p += 2*(dy-dx)
    x += 1
pt.plot(xp,yp,marker="P")
hr=datetime.datetime.now().hour
mn=datetime.datetime.now().minute
sec=datetime.datetime.now().second
if hr < 12:
    pt.savefig(f"{hr}-{mn}-{sec} AM.png")
elif hr == 12:
    pt.savefig(f"{hr}-{mn}-{sec} PM.png")
else:
    pt.savefig(f"{hr-12}-{mn}-{sec} PM.png")
pt.show()
