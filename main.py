import time
# Suma, resta, multiplicacion y division de numeros
# Funciones del programa
def sumar(lista, resultado):
 for num in lista:
  resultado += num
 print("La suma es: ", end = "")
 print(resultado)
def restar(lista, resultado):
 resultado = lista[0]
 for num in lista:
  if resultado == lista[0]:
   lista[0] = ""
   continue
  else:
   resultado -= num
 print("La resta es: ", end = "")
 print(resultado)
def multiplicar(lista, resultado):
 resultado += 1
 for num in lista:
  resultado *= num
 print("El producto es: ", end = "")
 print(resultado)
def dividir(lista, resultado):
 resultado = lista[0]
 for num in lista:
  if resultado == lista[0]:
   lista[0] = ""
   continue
  else:
   resultado /= num
 print("El cociente es: ", end = "")
 print(resultado)
def lineaDecorativa():
 print ("=" * 53)
def opciones():
 print("¿Qué opción desea escoger?")
 print("1. Sumar")
 print("2. Restar")
 print("3. Multiplicar")
 print("4. Dividir")
 time.sleep(0.5)
def aviso():
 time.sleep(0.5)
 print("Tenga en cuenta que se ira realizando la operación elegida, en base al orden de los numeros que introduzca")
 time.sleep(0.5)
 print("Ejemplo: Si desea restar dos numeros, 2 y 3, si coloca primero el 2 y luego el 3, entonces el resultado será -1 mientras que si lo coloca al reves, entonces tendrá como resultado 1")
 time.sleep(0.5)
# Variables principales de las funciones
listaOpciones = [
 [1, "sumar", sumar],
 [2, "restar", restar],
 [3, "multiplicar", multiplicar],
 [4, "dividir", dividir]
]
# Inicio del programa
time.sleep(0.5)
lineaDecorativa()
time.sleep(0.5)
print("  Suma, resta, multiplicación y división de numeros")
time.sleep(0.5)
lineaDecorativa()
time.sleep(0.5)
print("¡Hola! ", end = "")
respuesta = "si"
# Funcionamiento del programa (en bucle) hasta que el usuario lo termine
while respuesta == "si":
 time.sleep(1)
 opciones()
 print("Si desea escoger alguna opción, solo escriba el número que le corresponde a la opción deseada")
 opcion = int(input())
 aviso()
# Introducción de la cantidad de numeros que se desean operar
 print("¿Cuántos numeros desea " + listaOpciones[opcion - 1][1] + "?")
 i = int(input())
 j = 1
 numeros = []
# Introducción de los numeros que se van a operar
 while i > 0:
  print("Introduzca el número " + str(j) + " : ", end = "")
  numero = int(input())
  numeros.append(numero)
  j += 1
  i -= 1
 time.sleep(1)
# Operación e impresión de los numeros en consola
 print("Realizando la operación...")
 time.sleep(0.2 * len(numeros))
 funcionElegida= listaOpciones[opcion - 1][2]
 funcionElegida(numeros, 0)
 time.sleep(0.5)
 print("¿Desea realizar otra operación? (Si/No)")
 respuesta = input().lower()
# Fin del programa (y del bucle)
time.sleep(0.5)
print("Muchas gracias por usar el programa :D")