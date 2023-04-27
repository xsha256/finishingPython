def primo(entrada):
    try:
        num = int(entrada)
        divisor = num - 1
        res = ()
        if num < 0:
            res = "Solo son numeros primos aquellos enteros divisibles entre ellos y 1. Por tanto, ningún número negativo será primo."
        elif num == 0:
            res = "0 no es primo porque no se puede dividir."
        elif num == 1:
            res = "1 no es primo porque no tiene más de un divisor."
        elif num == 2 or num == 3:
            res = (f"El numero {num} ¡Es primo!")
        elif num > 3:
            while divisor != 1:
                temp = num %divisor
                if temp != 0:
                    divisor -= 1
                if temp == 0:
                    res = (f"{num} no es un número primo.")
                    break
            if res == ():
                res = (f"¡{num} es un número primo!")
    except:
        res = "El valor introducido no es correcto."
    return res
if __name__ == "__main__":
    entrada = input()
    primo(entrada)