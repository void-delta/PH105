from numpy import *
from matplotlib import *
from pylab import *

A = matrix([[2, 0, 0], [0, 4, 5], [0, 4, 3]])
x = eig(A)
print(x)