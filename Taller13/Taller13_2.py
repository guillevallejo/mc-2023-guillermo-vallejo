filas_a = int(input("Ingrese el número de filas de la matriz A: "))
columnas_a = int(input("Ingrese el número de columnas de la matriz A: "))
filas_b = int(input("Ingrese el número de filas de la matriz B: "))
columnas_b = int(input("Ingrese el número de columnas de la matriz B: "))

A = []
for i in range(filas_a):
    fila = []
    for j in range(columnas_a):
        fila.append(0)
    A.append(fila)

B = []
for i in range(filas_b):
    fila = []
    for j in range(columnas_b):
        fila.append(0)
    B.append(fila)

print("Ingrese los valores de la matriz A:")
for i in range(filas_a):
    for j in range(columnas_a):
        valor = float(input(f"A[{i+1}][{j+1}]: "))
        A[i][j] = valor

print("Ingrese los valores de la matriz B:")
for i in range(filas_b):
    for j in range(columnas_b):
        valor = float(input(f"B[{i+1}][{j+1}]: "))
        B[i][j] = valor

if filas_a == filas_b and columnas_a == columnas_b:
    
    tres_a = []
    for i in range(filas_a):
        fila = []
        for j in range(columnas_a):
            fila.append(3 * A[i][j])
        tres_a.append(fila)

    
    cuatro_b = []
    for i in range(filas_b):
        fila = []
        for j in range(columnas_b):
            fila.append(4 * B[i][j])
        cuatro_b.append(fila)

    
    suma_ab = []
    for i in range(filas_a):
        fila = []
        for j in range(columnas_a):
            fila.append(A[i][j] + B[i][j])
        suma_ab.append(fila)

    
    producto_ba = []
    for i in range(filas_b):
        fila = []
        for j in range(columnas_a):
            valor = 0
            for k in range(filas_a):
                valor += B[i][k] * A[k][j]
            fila.append(valor)
        producto_ba.append(fila)

    
    print("3A = ")
    print(tres_a)
    print("4B = ")
    print(cuatro_b)
    print("A + B = ")
    print(suma_ab)
    print("B x A = ")
    print(producto_ba)
else:
    print("Las matrices no tienen las mismas dimensiones, no se pueden realizar las operaciones.")