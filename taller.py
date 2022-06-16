from os import system

productos = []

salir = False
while salir == False:
     print('0. Salir')
     print('1. Registrar producto ')
     print('2. Mostrar listado de productos')
     print('3. Cambiar el nombre de un producto')
     print('4. Eliminar producto')
     seguir = False
     opcion = int(input('Opción: '))
     if 0 <= opcion <= 4:
         seguir = True
         print('Opción incorrecta')

     if seguir == True:
         if opcion == 0:
             salir = True
             print('Fin del Programa')

         elif opcion == 1:
             producto = input('Nombre del producto: ')
             if producto in productos:
                 print('El producto ya fue registrado anteriormente')
             else:
                 productos.append(producto)
                 print('Producto agregado de manera exitosa')

         if opcion == 2:
             if len(productos) > 0:
                 for i in productos:
                     indice = productos.index(i)
                     print(indice + 1, '.', productos[indice])
                 system('pause')

         if opcion == 3:
             busqueda = input('Buscar: ')
             cambio = False
             for i in productos:
                 if i == busqueda:
                     nuevoNombre = input('Nombre nuevo: ')
                     indice = productos.index(i)
                     productos[indice] = nuevoNombre
                     cambio = True

             if cambio == True:
                 print('Cambio exitoso')
             else:
                 print('Producto no encontrado')

         if opcion == 4:
             busqueda = input('Buscar: ')
             eliminar = False
             for i in productos:
                 if i == busqueda:
                     producto = productos.index(i)
                     productos.pop(producto)
                     eliminar = True

             if eliminar == True:
                 print('El producto se eliminó de manera exitosa')
             else:
                 print('Producto no encontrado')


'''Leer el año de nacimiento de 10 estudiantes del curso de Globant y calcular cuantos años
cumple cada estudiante en 2022 , finalmente indique cuantos estudiantes tiene mas de 22 años'''


from datetime import date

current_year = date.today().year

fechas_estudiantes = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005]


def edad_actual():
    estudiantes_mayores = 0
    years = [current_year - fecha for fecha in fechas_estudiantes]
    for fechas in years:
        if fechas > 22:
            estudiantes_mayores += 1
    return estudiantes_mayores


print(edad_actual())

'''Construir un programa que permita ingresar N (cantidad digitada por el usuario)
numeros enteros y cuente cuantos son multiplos de 2, de 3 y cuantos negativos fueron
ingresados'''

numMul2 = []
numMul3 = []
numNegativos = []

n = int(input('Ingrese la cantidad de números que desea registrar: '))

for a in range(n):
    numero = int(input('Ingrese un número entero: '))

    if numero % 3 == 0 and numero % 2 == 0 and numero < 0:
        numMul3.append(numero)
        numMul2.append(numero)
        numNegativos.append(numero)
    elif numero % 3 == 0 and numero < 0:
        numMul3.append(numero)
        numNegativos.append(numero)
    elif numero % 2 == 0 and numero < 0:
        numMul2.append(numero)
        numNegativos.append(numero)
    elif numero < 0:
        numNegativos.append(numero)
    elif numero % 3 == 0:
        numMul3.append(numero)
    elif numero % 2 == 0:
        numMul2.append(numero)

print('Números multiplos de 2:\n')
if len(numMul2) > 0:
    for a in numMul2:
        print(a)

print('\nNúmeros multiplos de 3:\n')
if len(numMul3) > 0:
   for a in numMul3:
       print(a)

print('Números negativos:\n')
if len(numNegativos) > 0:
    for a in numNegativos:
        print(a)
