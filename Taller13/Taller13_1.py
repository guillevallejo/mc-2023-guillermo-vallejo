n = int(input("Ingrese la longitud de los vectores: "))

vector1 = []
vector2 = []

for i in range(n):
    valor1 = float(input(f"Ingrese el valor {i+1} del primer vector: "))
    vector1.append(valor1)
    
    valor2 = float(input(f"Ingrese el valor {i+1} del segundo vector: "))
    vector2.append(valor2)

producto_escalar = 0
for i in range(n):
    producto_escalar += vector1[i] * vector2[i]

print(f"El producto escalar de los vectores {vector1} y {vector2} es {producto_escalar}")