import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])

y = x**2
plt.plot(y, x)

plt.title('My Pehla Graph')
plt.xlabel('x')
plt.ylabel('y')

plt.show()