def mayormenor0(entrada):
    #Algoritmo numeroCero
    # Entrada
    num = (entrada).replace(",",".").split(" ")
    # Proceso
    if len(num) != 1:
        res = "¡Solo un valor a la vez, por favor!"
    else:
        numero = float(num[0])
        if numero < 0:
            res = f"{numero} es menor que 0."
        elif numero > 0:
            res = f"{numero} es mayor que 0."
        elif numero == 0:
            res = f"{numero} es 0, jajaja justo 0."
    # Salida
    return res
if __name__ == "__main__":
    entrada = input()
    mayormenor0(entrada)