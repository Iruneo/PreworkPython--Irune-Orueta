
def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return "División por cero no válida"

def potencia(numero1, numero2):
    return numero1 ** numero2

def raiz_cuadrada(numero):
    if numero >= 0:
        return numero ** 0.5
    else:
        return "Raíz cuadarada menor que cero no válida"

def calculadora():
    print("Bienvenido a la calculadora")
    resultado = 0
    while (True):
        

        # print("0. Reutilizar resultado anterior")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raiz Cuadrada")
        print("7. Salir")

        eleccion = input("Selecciona la operación que quieres realizar(1/2/3/4/5/6/7): ")
        if eleccion == "7":
            print("¡Hasta luego!")
            break

        elif eleccion in ["1", "2", "3", "4", "5", "6"]:
            if resultado == 0:
                if eleccion != "6":
                    numero1 = int(input("Introduce un numero para operar: "))
                    numero2 = int(input("Introduce otro numero para operar: "))

                    if eleccion == "1":
                        resultado = suma(numero1, numero2)
                        print(f"El resultado de la operacion {numero1} + {numero2} es: ", resultado)
                    elif eleccion == "2":
                        resultado = resta(numero1, numero2)
                        print(f"El resultado de la operacion {numero1} - {numero2} es: ", resultado)
                    elif eleccion == "3":
                        resultado = multiplicacion(numero1, numero2)
                        print(f"El resultado de la operacion {numero1} * {numero2} es: ", resultado)
                    elif eleccion == "4":
                        resultado = division(numero1, numero2)
                        print(f"El resultado de la operacion {numero1} dividido por {numero2} es: ", resultado)
                    elif eleccion == "5":
                        resultado =  potencia(numero1, numero2)
                        print(f"El resultado de la operacion {numero1} elevado a {numero2} es: ",resultado)
                else:
                    numero1 = int(input("Introduce un umero para operar: "))
                    print(f"El resultado de la operacion raíz cuadrada de {numero1} es: ", raiz_cuadrada(numero1))
                    resultado = raiz_cuadrada(numero1)

            else:
                if eleccion != "6":
                    numero2 = int(input("Introduce otro numero para operar: "))
                    if eleccion == "1":
                        print(f"El resultado de la operacion {resultado} + {numero2} es: ", suma(resultado, numero2))
                        resultado = suma(resultado, numero2)
                    elif eleccion == "2":
                        print(f"El resultado de la operacion {resultado} - {numero2} es: ", resta(resultado, numero2))
                        resultado = resta(resultado, numero2)
                    elif eleccion == "3":
                        print(f"El resultado de la operacion {resultado} * {numero2} es: ", multiplicacion(resultado, numero2))
                        resultado = multiplicacion(resultado, numero2)
                    elif eleccion == "4":
                        print(f"El resultado de la operacion {resultado} dividido por {numero2} es: ", division(resultado, numero2))
                        resultado = division(resultado, numero2)
                    elif eleccion == "5":
                        print(f"El resultado de la operacion {resultado} elevado a {numero2} es: ",potencia(resultado, numero2))
                        resultado =  potencia(resultado, numero2)
                else:
                    print(f"El resultado de la operacion raíz cuadrada de {resultado} es: ", raiz_cuadrada(resultado))
                    resultado = raiz_cuadrada(resultado)


            acumular = input("Quieres reutilizar el resultado? Y/n: ").lower()

            if acumular == "n":
                resultado = 0

            elif acumular != "y":
                print("Opcion no valida. No se acumula valor")
                resultado = 0

        else: 
            print("Elección no valida")

if __name__ == "__main__":
    calculadora()



      