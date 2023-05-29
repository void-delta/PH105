from numpy import *
from matplotlib import *
from pylab import *

x = array([1,2,3,5,7])
y = x + 6

plot(x, y, 'rx')
title('Array and Output')
xlabel('Array')
ylabel('Output')
show()