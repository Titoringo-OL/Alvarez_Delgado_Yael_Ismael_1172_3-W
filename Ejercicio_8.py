#Ingresar un número natural por teclado. Se desea saber y mostrar
#si es par o impar.
print("Alvarez Delgado Yael Ismael 1172 3-W: Ejercicio #8")
print(" ") 
#Pedimos al usuario que ingrese un numero
numero = int(input('Ingrese un numero:'))
#Damos condiciones para saber si es par o impar
if numero % 2 == 0: #Un número es par si el residuo de dividirlo entre 2 es 0, es decir, numero % 2 == 0.
    print("El número es par.")
else: #Cualquier número que no sea divisible por 2 sin dejar residuo es impar.
    print("El número es impar.")