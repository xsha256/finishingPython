def volumencubo(entrada):
    #Algoritmo AreaVolumenCubo
    # Entrada
    lado = int(entrada)
    # Proceso
    cuadrado = lado * lado
    area = cuadrado * 6
    volumen = cuadrado * lado
    # Salida
    res = f"El Área de un cuadrado de lado {lado} es = {area}.<br>El volumen de un cuadrado de lado {lado} es = {volumen}"
    return res
if __name__ == "__main__":
    entrada = input()
    volumencubo(entrada)