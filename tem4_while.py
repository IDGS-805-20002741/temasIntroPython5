# ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
# Bucles con While.
# Fecha: 14-01-2025.
# ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨

print("Ingresa el numero para ver sus multiplicadores.")

num1 = input('Numero: ')
x = 1
resultado = 0

while x <= 10:
    resultado = int(num1) * x
    print("{} x {} = {}".format(num1,x,resultado))
    x += 1