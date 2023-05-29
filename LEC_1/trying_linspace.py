from numpy import *
from matplotlib import *
from pylab import *

x = linspace(0, 20, 11)
print(x)
y = x + 2
plot(x, y, color = 'orange', marker = '*' )
xlabel('Using Linspace')
ylabel('Output')
title("Array Linspace")

show()