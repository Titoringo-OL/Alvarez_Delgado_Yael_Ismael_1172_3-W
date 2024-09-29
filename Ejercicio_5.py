print("Alvarez Delgado Yael Ismael 1172 3-W: Ejercicio #5")
print(" ") 
print("Desarrollar código que lea dos valores que captures, determinar cual de los dos valores es el menor y escríbalo")
# Pedimos al usuario que ingrese los valores
a = int(input('Ingrese el primer valor:')) #Se usa para pedir datos de entrada al usuario
b = int(input('Ingrese el segundo valor:')) #Se usa para pedir datos de entrada al usuario
#Aplicamos las condiciones para saber cual es el menor
if a < b:
  print(f'{a} es el valor menor')
elif b < a:
  print(f'{b} es el valor menor')
print(" ")
print("Realizar un algoritmo que sume dos números y desplegarlo")
print(" ") 
#Pedimos al usuario que ingrese dos numeros
c = int(input('Ingrese el primer numero:')) #Se usa para pedir datos de entrada al usuario
d = int(input('Ingrese el segundo numero:')) #Se usa para pedir datos de entrada al usuario

s = c + d #Operacion aritmetica
print(f'La suma de {c} y {d} es:',s) #Esto se mostrara en pantalla
  
