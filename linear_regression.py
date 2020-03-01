"""Draw Linear Regression."""

import numpy as np
import matplotlib.pyplot as plt

def drawLinearRegression(x, y):
    """Calculate and draw linear regression."""
    #plt.ion() # Interactive plt
    coeffs = np.polyfit(x, y, 1)
    m = coeffs[0]
    b = coeffs[1]
    est_y = (m * x) + b
    print(f'm= {m}, b={b}, x={x}\n (m*x)+b')
    plt.plot(x, est_y)
    plt.scatter(x, y)
    plt.draw()
    plt.show()

if __name__ == "__main__":
    x = np.array(np.arange(0,9))
    y = np.array([1, 2, 3, 5, 4, 6, 8, 7, 9])

    drawLinearRegression(x, y)