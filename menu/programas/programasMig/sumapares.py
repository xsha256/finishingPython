def sumapares(entrada):
    #Algoritmo SumaNumerosPares
    # Entrada
    lista = (entrada).replace(" y ",",").split(",")
    listalimp = []
    suma = 0
    # Proceso
    try:
        for i in range(len(lista)):
            listalimp.append(int(lista[i]))
        for j in range(len(listalimp)):
            if listalimp[j] %2 == 0:
                suma = suma + listalimp[j]
        # Salida
        res =f"La suma de los elementos pares de la lista es {suma}."
    except:
        res = "Los elementos introducidos son erroneos.<br>Pruebe a introducir números separados por comas."
    return res
if __name__ == "__main__":
    entrada = input()
    sumapares(entrada)