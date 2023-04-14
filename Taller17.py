import numpy as np

def exp_regre(x, y):
    log_y = np.log(y)
    m, b = np.polyfit(x, log_y, 1)
    b = np.exp(b)
    return m, b

x = np.array([1,2,3,4,5])
y = np.array([5,6.6,8.5,10.8,14.2])

m, b = exp_regre(x, y)

print("La línea ajustada es: y = {:.6f} * exp({:.6f}x)".format(b, m))
print("")
plt.plot(x, y, label="línea L")
plt.plot()
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.title("Gráfico en líneas de ejemplo")
plt.legend()
plt.show()
