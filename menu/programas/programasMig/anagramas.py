#Algoritmo Anagramas
# Entrada
def anagramas(entradaA, entradaB):
    cadenaa = (entradaA).strip()
    cadenab = (entradaB).strip()
    cadena1 = []
    cadena2 = []
    # Proceso
    for letra in cadenaa:
        cadena1.append(letra)
    for letra in cadenab:
        cadena2.append(letra)
    cadena1.sort()
    cadena2.sort()
    if cadena1 == cadena2:
        res = f"{cadenaa} y {cadenab} son anagramas :)"
    else:
        res = f"{cadenaa} y {cadenab} no son anagramas :("
    return res
if __name__ == "__main__":
    entrada = input()
    anagramas(entrada)