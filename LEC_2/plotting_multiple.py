from numpy import *
from matplotlib import *
from pylab import *

x = linspace(0, 20, 121)
y1 = (x**4)*exp(-2*x)
y2 = (x**2)*exp(-x)*sin(x**2)
plot(x, y1, 'y^')
plot(x, y2, 'r-')
show()