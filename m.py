import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,10])
y=np.array([0,100])
# plt.plot(x,y)
# plt.show()


# marker


# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline
# yp=np.array([0,5,0,-5,0,5,0,-5,0])
# plt.plot(yp,marker='X')
# plt.show()


#linestyle or ls


# solid' (default)	'-'	
# 'dotted'	':'	
# 'dashed'	'--'	
# 'dashdot'	'-.'	
# 'None'	'' or ' '	
# yp=np.array([0,5,0,-5,0,5,0,-5,0])
# plt.plot(yp,marker='h',ls=':')
# plt.show()

#labels and title

yp=np.array([0,5,0,-5,0,5,0,-5,0])
plt.plot(yp,marker='h',ls=':')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Graph between X-Axis and Y-Axis")
plt.grid(linewidth="1.0",color='b')
plt.show()
