# ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
# Metodos y funciones.
# Fecha: 14-01-2025.
# ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨

import os

def funcion1():
    os.system('cls')
    print("Suma de dos numeros.")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))

    suma = num1 + num2
    print("La suma de {} y {} es {}".format(num1,num2,suma))

def funcion2():
    os.system('cls')
    print("Hola Mundo!")

def run():
    os.system('cls')
    print("Menu de opciones: ")
    print("1. Suma de dos numeros")
    print("2. Otra opcion")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        funcion1()
    if opcion == 2:
        funcion2()

if __name__ == "__main__":
    run()