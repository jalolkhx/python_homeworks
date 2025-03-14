import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label="$ \sin(x) $", color='red', linestyle='-.', marker='*')
plt.plot(x, y2, label="$ \cos(x) $", color='cyan', linestyle=':', marker='.')
plt.legend()
plt.show()