from numpy import *
from matplotlib import *
from pylab import *

frequency, mic1, mic2 = loadtxt('gangu.txt', unpack = True)

# the unpack will tell the python to read the data and store it in the form of 'Arrays'
figure()
plot(frequency, mic1, 'r-', frequency, mic2, 'b-')
xlabel('FREQUENCY(Hz)')
show()