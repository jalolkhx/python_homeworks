import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.cos(x*x + y*y)

ax.plot3D(x, y, z, c='pink')
ax.set_title('3D sample')
plt.show()