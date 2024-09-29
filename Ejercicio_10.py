print("Alvarez Delgado Yael Ismael 1172 3-W: Ejercicio #10")
print(" ") 
# Solicitar un número entero al usuario
N = int(input("Ingresa un número entero para calcular su factorial: "))

# Inicializar el factorial en 1 (porque el factorial de 0 es 1)
factorial = 1

# Verificar si el número es no negativo
if N >= 0:
    # Calcular el factorial usando un bucle
    for i in range(1, N + 1):
        factorial *= i
    print(f"El factorial de {N} es: {factorial}")
else:
    print("El número debe ser no negativo.")

