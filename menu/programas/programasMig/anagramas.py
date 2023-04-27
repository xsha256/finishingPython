#Algoritmo Anagramas
# Entrada
def anagramas(entrada):
    textobruto = entrada.lower().split(".")
    if len(textobruto) == 2:
        cadenaa = (textobruto[0]).strip()
        cadenab = (textobruto[1]).strip()
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
    else:
        res = "Valores introducidos incorrectos.<br>Prueba a escribir las dos frases separadas por un punto."
    return res
if __name__ == "__main__":
    entrada = input()
    anagramas(entrada)