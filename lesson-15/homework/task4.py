import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, color = 'red', marker = 'o')
plt.title("Sample of scatter")
plt.show()