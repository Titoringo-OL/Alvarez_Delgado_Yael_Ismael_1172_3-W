#Solicitar al usuario un número natural y verificar que el número
#ingresado se encuentre dentro de la primera docena de números naturales,
#es decir entre el 1 y el 12.
print("Alvarez Delgado Yael Ismael 1172 3-W: Ejercicio #7")
print(" ") 
#Pedimos al usuario que ingrese un numero natural
a = int(input('Ingrese un numero natural:'))
print(" ")
#Damos condiciones para que este en el rango que se desea
if a >= 1 and  a <= 12:
  print(f'El numero {a} esta dentro del rango')
else:
    print(f'El numero {a} esta fuera de rango')