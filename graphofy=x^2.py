#y=x**2
import matplotlib.pyplot as plt
import numpy as np
xp=[]
yp=[]
for i in range(9):
    y=i*i
    xp.append(i)
    yp.append(y)
a=np.array(xp)
b=np.array(yp)
plt.plot(a,b,marker=".")
plt.title("y=x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()