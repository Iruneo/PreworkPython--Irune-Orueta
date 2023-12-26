"""
1. Ejercicio: Define una función que tome dos números y retorne su suma. 2. Ejercicio: Defineuna función que tome un número y retorne su factorial. 
3. Ejercicio: Define una función que tome un número y determine si es primo. 
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos. 
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa. 
"""

def suma(a, b):
  return a + b
resultado = suma(2, 8)
print(resultado)

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
num = 5
print("Factorial of", num, "is", factorial(num))

num=13 
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
es_primo(num)



cadena = "lunes"
cadena_invertida = cadena[::-1]
print(cadena_invertida) 














