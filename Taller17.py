import numpy as np
import matplotlib.pyplot as plt

def exponential_regression(x, y):
    log_y = np.log(y)
    m, b = np.polyfit(x, log_y, 1)
    b = np.exp(b)
    return m, b

x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([2.2, 3, 4.5, 6, 8.5, 12])

m, b = exponential_regression(x, y)

print("La línea ajustada es: y = {:.5f} * exp({:.5f}x)".format(b, m))

plt.scatter(x, y)
x_fit = np.linspace(x[0], x[-1], 100)
y_fit = b * np.exp(m * x_fit)
plt.plot(x_fit, y_fit, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Modelo exponencial ajustado')
plt.show()
