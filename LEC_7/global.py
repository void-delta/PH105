from numpy import *
from matplotlib import *
from pylab import *

a = 4
b = 5
c = 6

def fn(a):
    d = a
    a = b
    global c 
    c = 9
    return d
print(a, b, fn(a), fn(b), fn(c), c)

