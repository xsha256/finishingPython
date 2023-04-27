#Algoritmo norepe
# Entrada
def duplicados(entrada):
    lista = entrada.replace("y",",").split(",")
    listaint = []
    # Proceso
    try:
        for i in range(len(lista)):
            listaint.append(int(lista[i]))
        listaint = set(listaint)
        listaint = list(listaint)
        res = f"Su lista sin elementos repetidos es:<br>{listaint}"
    except:
        res = "Los valores introducidos no son correctos. Inténtelo de nuevo introduciendo números separados por comas."
    return res
if __name__ == "__main__":
    entrada = input()
    duplicados(entrada)