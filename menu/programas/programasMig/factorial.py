def factorial(valor):
    lista = []
    resultado = 1
    i = 0
    num = int(valor)
    for i in range(num -1, -1, -1):
        lista.append(num)
        num = num - 1
        i = i - 1
    for i in range(len(lista) - 1, -1, -1):
        resultado = resultado * lista[i]
    res = f"factorial({valor}) = {resultado}."
    # Salida
    return res
if __name__ == "__main__":
    valor = input()
    factorial(valor)