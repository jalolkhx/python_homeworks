import numpy as np
import matplotlib.pyplot as plt

# Generate x values for each function
x1 = np.linspace(-2, 2, 400)
y1 = x1**3

x2 = np.linspace(0, 2 * np.pi, 400)
y2 = np.sin(x2)

x3 = np.linspace(-2, 2, 400)
y3 = np.exp(x3)

x4 = np.linspace(0, 2, 400)
y4 = np.log(x4 + 1)

# Create the subplots
fig, axs = plt.subplots(2, 2)

# Top-left: Cubic function
axs[0, 0].plot(x1, y1, color='r')
axs[0, 0].set_title('$f(x) = x^3$')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')
axs[0, 0].grid(True)

# Top-right: Sine function
axs[0, 1].plot(x2, y2, color='b')
axs[0, 1].set_title('$f(x) = \sin(x)$')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')
axs[0, 1].grid(True)

# Bottom-left: Exponential function
axs[1, 0].plot(x3, y3, color='g')
axs[1, 0].set_title('$f(x) = e^x$')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')
axs[1, 0].grid(True)

# Bottom-right: Logarithm function
axs[1, 1].plot(x4, y4, color='m')
axs[1, 1].set_title('$f(x) = \log(x+1)$')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')
axs[1, 1].grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
