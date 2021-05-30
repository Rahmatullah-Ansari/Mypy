import matplotlib.pyplot as plt
import numpy as np
yp=np.array([])
x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))
dx=abs(x2-x1)
dy=abs(y2-y1)
if dx>=dy:
    step=dx
else:
    step=dy
xinc=float((x2-x1)/step)
yinc=float((y2-y1)/step)
i=0
x=x1
y=y1
lst=[]
lyt=[]
while i<=step:
    lst.append(x)
    lyt.append(y)
    x += xinc
    y += yinc
    i += 1
xp=np.array(lst)
yp=np.array(lyt)
plt.plot(xp,yp,marker='X')
plt.show()