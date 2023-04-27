#Algoritmo mediadelista
# Entrada
def medialista(entrada):
    lista = (entrada).replace("y",",").split(",")
    listalimp = []
    suma = 0
    # Proceso
    try:
        for i in range(0,len(lista)):
            listalimp.append(int(lista[i]))
        for j in range(len(listalimp)):
            suma = listalimp[j] + suma
        res = suma / len(listalimp)
        # Salida
        salida = (f"Número de elementos proporcionados: {len(listalimp)} <br>Suma de todos los elementos: {suma}<br>La media de los elementos es {res}.")
    except:
        salida = "Valores introducidos inválidos. Asegúrese de ingresar números separados por comas."
    return salida
if __name__ == "__main__":
    entrada = input("dae: ")
    medialista(entrada)