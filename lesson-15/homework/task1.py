import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = x** - 4*x + 4
plt.figure(figsize=(5, 5))
plt.plot(x, y, label="$ f(x) = x^2 - 4x + 4 $")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the Function $f(x) = x^2 - 4x + 4$')

plt.legend()
plt.show()