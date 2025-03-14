import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='red', color='green', alpha=0.7)
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("x")
plt.ylabel("y")

plt.show()