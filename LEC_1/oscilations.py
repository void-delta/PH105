from numpy import *
from matplotlib import *
from pylab import *

time = linspace(0.0, 10.0, 100)
height = exp(-time/3.0)*sin(time*3)
figure()
plot(time, height, color = 'orange', marker = '^')
plot(time, 0.3*sin(time*3), 'g-')
legend(['damped', 'constant amplitude'], loc = 'upper right')
xlabel('Time(s)')
show()