print("Alvarez Delgado Yael Ismael 1172 3-W: Ejercicio #4")
print(" ") 
# Leer los valores
A = int(input("Introduce el primer valor (A): "))
B = int(input("Introduce el segundo valor (B): "))
C = int(input("Introduce el tercer valor (C): "))

# Comprobar si los valores son distintos
if A == B or A == C or B == C:
    print("Error: Todos los valores deben ser distintos.")
else:
    # Determinar el mayor y el menor
    mayor = max(A, B, C)
    menor = min(A, B, C)

    # Imprimir resultados
    print("El mayor es:", mayor)
    print("El menor es:", menor)
