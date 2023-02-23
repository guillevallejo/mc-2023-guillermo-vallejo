import math

def c_a(x, eps):
    cos_x = 1
    y = -1
    i = 2
    valor_ant = 1
    error_abs = eps + 1
    intera = 0
    while error_abs > eps:
        valor_act = y * (x**i) / math.factorial(i)
        cos_x += valor_act
        y *= -1
        i += 2
        error_abs = abs(valor_act - valor_ant)
        valor_ant = valor_act
        intera += 1
    return cos_x, intera

x = float(input("Ingrese el valor en radianes: "))
eps = float(input("Ingrese el criterio de error esperado (con 8 cifras significativas): "))
cos_x_aprox, intera = c_a(x, eps)
error_relativo = abs(math.cos(x) - cos_x_aprox) / abs(math.cos(x)) * 100
print("El coseno de {} es aproximadamente {:.8f}".format(x, cos_x_aprox))
print("El error aproximado relativo porcentual es {:.8f}%".format(error_relativo))
print("El número de intera realizadas fue {}".format(intera))
