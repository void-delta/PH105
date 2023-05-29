from numpy import *
from matplotlib import *
from pylab import *

A = matrix([[-13, 2, 4], [2, -11, 6], [4, 6, -15]])
B = array([5, -10, 5])
k = linalg.solve(A, B)
print(k)