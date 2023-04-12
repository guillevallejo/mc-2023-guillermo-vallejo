import numpy as np

def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    xy_mean = np.mean(x * y)
    x_squared_mean = np.mean(x**2)

    m = (xy_mean - x_mean * y_mean) / (x_squared_mean - x_mean**2)
    b = y_mean - m * x_mean

    return m, b
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([3.5, 2.5, 3, 1.5, 2, 1.3, 1, 0.3])

m, b = linear_regression(x, y)

print("La línea ajustada es: y = {:.5f}x + {:.5f}".format(m, b))
