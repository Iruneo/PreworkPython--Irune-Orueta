"""Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci. """

"""Define una función que tome un número y retorne una lista de sus divisores. """
def divisores(n):
  return [i for i in range(1, n+1) if n % i == 0]
print (divisores (20))

"""Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original. """

def unicos(lista):
  return list(set(lista))
print(unicos([1,3,3,6,7,7,9,12,12]))

"""Define una función que tome un número y retorne la suma de sus dígitos."""

def suma_digitos(n):
  return sum(int(digito) for digito in str(n))
print(suma_digitos(426))

"""Define una función que tome una cadena y cuente el número de vocales en la cadena. """
def contar_vocales(cadena):
    return sum(c in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"} for c in cadena)
print (contar_vocales('Feliz Año Nuevo'))

"""Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista."""

"""Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena."""
def contar_mayusculas_minusculas(cadena):
   mayusculas = sum(1 for letra in cadena if letra.isupper())
   minusculas = sum(1 for letra in cadena if letra.islower())
   return mayusculas, minusculas
print(contar_mayusculas_minusculas ("Buenos Dias")) 

"""Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3."""

   
""" Define una función que reciba un número y retorne su representación en binario."""
def binario(numero):
   resultado=()
   while numero !=1:
      resultado.append(numero%2)
      numero = int(numero/2)
      if numero == 1:
         resultado.append(numero)
   print(str(resultado[::-1]))
   binario(14)

"""Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas)."""

def interseccion(lista1, lista2):
   return list(set(lista1) & set(lista2))
print(interseccion([9,6,8,4,5], [6,9,3,5,2]))

"""Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""

def si_palindromo(cadena):
   return cadena == cadena[::-1]
print(si_palindromo("somos"))

"""Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”."""

def FizzBuzz(): 
   numero = 1
   while numero <= 50:
      if numero % 3 == 0 and numero % 5 == 0:
         print('FizzBuzz')
      elif numero % 3== 0:
         print('Fizz')
      elif numero % 5==0:
         print ('Buzz')
      else:
         print(numero)
      numero += 1
FizzBuzz()

"""Define una función que tome una lista y retorne la lista ordenada en orden ascendente."""
def ordenar_lista_ascendente(lista):
   return sorted(lista)
print(ordenar_lista_ascendente([9,6,2,4,1,0,16,5]))

""" Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n."""

def lista_palabras(lista_de_palabras,n):
   return[palabra for palabra in lista_de_palabras if len(palabra) > n]
print(lista_palabras(["mañana", "martes", "sol", "frio"], 3))

""" Define una función que tome un número y calcule su serie de Fibonacci."""

def Fibonacci(numero):
   if numero == 0:
      return False
   elif numero ==1:
      return 1
   return numero + Fibonacci(numero-1)

print (Fibonacci(18))
"""Define una función que tome una lista de números y retorne el número más grande de la lista."""

def maximo (lista):
   return max(lista)
print(maximo([2,6,9,12]))

"""Define una función que reciba un número y retorne la suma de sus dígitos al cubo."""
def suma_al_cubo_digitos(n):
   return sum(int(digit)**3 for digit in str(n)) 
print(suma_al_cubo_digitos(246))

"""Define una función que reciba una lista de números y retorne el segundo número más grande de la lista."""
def segundo_numero_mas_grande(lista):
   return sorted(set(lista), reverse = True)[1]
print(segundo_numero_mas_grande([2,7,4,13]))

"""Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False."""

def en_comun(lista1,lista2):
   return bool(set(lista1) & set(lista2))
print(en_comun([4,6,7,2],[5,4,2,9]))

"""Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso"""

def invertir_lista(lista):
   return lista[::-1]
print(invertir_lista([1,2,3,4,5,6]))

"""Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene."""

def contar_digitos_y_letras(cadena):
   digitos = 0
   letras = 0
   for c in cadena:
      if c.isdigit():
         digitos += 1
      elif c.isalpha():
         letras += 1
      else:
         pass
   return digitos, letras

print(contar_digitos_y_letras("Enero 2024"))

"""Define una función que reciba una lista de números y retorne la suma acumulada de los números"""

def suma_acumulada(lista):
   suma = 0
   for i in lista:
      suma = suma + i
   return suma
print(suma_acumulada([1,2,3,4,5,6])) 

"""Define una función que encuentre el elemento más común en una lista. """
from collections import Counter

def elemento_mas_comun(lista):
   return Counter(lista).most_common (1)[0][0]
print(elemento_mas_comun([1,2,3,4,4,2,2,5,6,6,5,3,7,2]))

""" Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10."""

def tabla_multiplicar(numero):
   return {i: numero * i for i in range (1,11)}  
print(tabla_multiplicar(3))

"""Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena."""

def contar_cantidad_caracteres(cadena):
   return {caracter: cadena.count(caracter) for caracter in cadena}
print(contar_cantidad_caracteres("bienvenido martes"))

"""Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas."""

def elementos_no_comunes(lista1, lista2):
   return list(set(lista1) ^ set(lista2))
print(elementos_no_comunes([1,2,3,4,5], [4,5,6,7,8]))

"""Define una función que tome una lista y retorne la lista sin duplicados"""
def sin_duplicados(lista):
   return list(set(lista))
print (sin_duplicados([1,1,2,3,4,4,5,6,7,7,8]))

"""Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número."""
def suma_cuadrados_pares(n):
   return sum(i**2 for i in range(2, n+1, 2))
print(suma_cuadrados_pares(9))

"""Define una función que reciba una lista de números y retorne el promedio de los números en la lista."""
def promedio(lista):
   return sum(lista) / len(lista)
print(promedio([1,2,3,4,5,6]))

"""Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista."""
def cadena_mas_larga(lista):
   return max(lista, key=len)
print(cadena_mas_larga(["hoy", "es", "martes"]))

"""Define una función que reciba un número entero n y retorne una lista con los n primeros números primos."""

"""Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso."""

def invertir_palabaras(cadena):
     return cadena[::-1]
print(invertir_palabaras("Hola, Buenos días"))

"""Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla."""

"""Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena."""
def cantidad_vocales(cadena):
   return sum(1 for c in cadena.lower() if c in 'aeiou')
print(contar_vocales("Hsta Mañana"))

"""Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False."""
def es_primo(num):
   if num < 2:
      return False
   for i in range (2, int(num ** 0.5)+1):
      if num % i == 0:
         return False
      return True
print (es_primo(22))

"""Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False."""
def es_primo(x):
   if x < 2:
      return False
   for num in range(2,x):
      if x % num == 0:
         return False
      return True  
print(es_primo(22)) 










