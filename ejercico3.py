"""
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for. 
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while. 
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
"""

for i in range(101):
  print(i)

x = 0
while x <= 100:
  if x%2 == 0:
    print(x)
    x = x + 2

x=1
z=0
while x<=100:
  print(x)
  z += x
  x +=1
  print(z)






