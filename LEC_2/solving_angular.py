from numpy import *
from matplotlib import *
from pylab import *

x = matrix([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
k = eigvals(x)
print(k)