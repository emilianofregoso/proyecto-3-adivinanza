import random

numero = random.randint(1, 100)
intentos = 0
max_intentos = 7

print("Juego de adivinanza")
print("Adivina un numero del 1 al 100")

while intentos < max_intentos:
    adivina = input("Escribe un numero: ")

    if not adivina.isdigit():
        print("Escribe un numero valido")
        continue

    adivina = int(adivina)

    if adivina < 1 or adivina > 100:
        print("El numero debe estar entre 1 y 100")
        continue

    intentos += 1

    if adivina == numero:
        print(f"Felicidades, adivinaste en {intentos} intentos")
        break
    elif adivina < numero:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")
else:
    print(f"Se acabaron los intentos. El numero era {numero}")

print("Fin del juego")
