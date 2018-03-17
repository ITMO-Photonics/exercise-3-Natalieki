import numpy as np
import matplotlib.pyplot as plt
import scipy.special.cython_special
x=np.linspace(0.,20.,2000)
y0 = scipy.special.jn(0,x)
y1 = scipy.special.jn(1,x)
y2 = scipy.special.jn(2,x)
y3 = scipy.special.jn(3,x)
y4 = scipy.special.jn(4,x)
y5 = scipy.special.jn(5,x)
y6 = scipy.special.jn(6,x)
fig, ax = plt.subplots()
ax.plot(x,y0,color='red',label='J0')
ax.plot(x,y1,color='orange',label='J1')
ax.plot(x,y2,color='yellow',label='J2')
ax.plot(x,y3,color='green',label='J3')
ax.plot(x,y4,color='cyan',label='J4')
ax.plot(x,y5,color='blue',label='J5')
ax.plot(x,y6,color='purple',label='J6')
ax.legend(loc='upper right')
plt.show()

