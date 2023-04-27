#Algoritmo AdivinaNumero
# Entrada
import random
nalea = random.randint(1,100)
intentos = 0
res = ()
print("Vamos a jugar a un juego. \nVoy a pensar un número del 1 al 100 \n¡A ver si eres capaz de adivinarlo!\nVenga, ¿Cuál es mi número?")
# Proceso
while res == ():
    nuser = int(input())
    intentos += 1
    if nuser < nalea:
        print("Es más grande. prueba de nuevo: ")
    elif nuser > nalea:
        print("Es más pequeño. prueba de nuevo: ")
    elif nuser == nalea:
        res = f"¡Ese es! Lo adivinaste en {intentos} intentos."
if intentos == 1:
    res = f"¡Qué máquina!¡Lo adivinaste a la primera!"
# Salida
print(res)