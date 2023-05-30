from numpy import *
from matplotlib import *
from pylab import *

def plotrig(f):
    xvaluse = linspace(-pi, pi, 100)
    plot(xvaluse, f(xvaluse))
    xlim(-pi, pi)
    ylim(-2, 2)

trigfunctions = (sin, cos, tan)

for function in trigfunctions:
    print(function(pi/6.0))
    plotrig(function)
    show()
