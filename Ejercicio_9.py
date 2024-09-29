print("Alvarez Delgado Yael Ismael 1172 3-W: Ejercicio #9")
print(" ") 
#Pedimos al usuario que ingrse un numero entero
numero = int(input("Ingresa un número entero: "))

#Verificar si es divisible por 7 y mayor a 40
if numero % 7 == 0 and numero > 40:
    print(f"El número {numero} es divisible por 7 y mayor que 40.")
else:
    print(f"El número {numero} no cumple con las condiciones.")