#Algoritmo numerosCapicúa
# Entrada
def capicua(entrada):
    num = entrada.split(" ")
    numpart = []
    lista = ["0","1","2","3","4","5","6","7","8","9"]
    numnum = []
    numin = []
    contador = False
    res = ()
    y = i = j = t = v = 0
    num = str(num)
    num = num.replace("[","")
    num = num.replace("]","")
    num = num.replace("'","")
    for letra in num:
        numpart.append(letra)
    for i in range(0,len(numpart),1):   
        for j in range(0,len(lista),1):
            if numpart[i] != lista[j]:
                contador = False
            if numpart[i] == lista[j]:
                contador = True
                break
    if contador == False:
        res = "Solo se admiten números"
# Proceso
    if res == ():
        for v in range(0,len(numpart),1):
            numnum.append(int(numpart[v]))
        for t in range((len(numnum)-1),-1,-1):
            numin.append(numnum[t])
        numnum = list(numnum)
        if numnum == numin:
            res = f"{num} es capicúa."
        else:
            res = f"{num} no es capicúa."
# Salida
    return res
if __name__ == "__main__":
    entrada = input()
    capicua(entrada)