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

"""Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas)."""

def interseccion(lista1, lista2):
   return list(set(lista1) & set(lista2))
print(interseccion([9,6,8,4,5], [6,9,3,5,2]))

"""Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""

def si_palindromo(cadena):
   return cadena == cadena[::-1]
print(si_palindromo("somos"))

"""Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”."""

"""Define una función que tome una lista y retorne la lista ordenada en orden ascendente."""
def ordenar_lista_ascendente(lista):
   return sorted(lista)
print(ordenar_lista_ascendente([9,6,2,4,1,0,16,5]))

""" Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n."""

def lista_palabras(lista_de_palabras,n):
   return[palabra for palabra in lista_de_palabras if len(palabra) > n]
print(lista_palabras(["mañana", "martes", "sol", "frio"], 3))

   
   








   




