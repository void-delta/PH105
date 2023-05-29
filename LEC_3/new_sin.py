from numpy import *
from matplotlib import *
from pylab import *

t = 30
A = matrix([[cos(t), -sin(t)], [sin(t), cos(t)]])
x = eig(A)
#print(x)

B = matrix([[2, -1], [4, 3]])
y = eig(B)
print(y)