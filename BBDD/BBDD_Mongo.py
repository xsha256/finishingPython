# Elegir uno de los ejercicios de ficheros y utilizar en cambio de ficheros la BBDD (Se puede elegir entre MongoDB o SQL Server).

# ### 1 - Lista de hombres y mujeres
# ### 2 - Lista de personas para por edades.
# ### 3 - Lista de Personas
# ### 4 - Temperatura mensual de 20 ciudades

# ## Condiciones:

# Deberá completar su programa en Python para que cumpla con las siguientes condiciones:

# - Mostrar una opción para generar los datos de forma aleatoria y almacenarlo en la BBDD.
# - Mostrar una opción para recuperar los datos de la BBDD (si existe) o generarlos de nuevo y almacenarlos en la BBDD.
# - Realice la opción para que el resultado de las opciones estadísticas se puedan guardar en la BBDD.

''' #! 1 - Lista de hombres y mujeres
# ¿ Crear un programa en Python para generar aleatoriamente una lista de 100 elementos que representan el género de las personas: "H" para hombres y "M" para mujeres.
# ¿ Llamar a una función llamada "ClasificarGenero" pasando la lista de personas como argumento. La función "ClasificarGenero" clasifica y cuenta la cantidad de hombres y mujeres en la lista, calcula el porcentaje de hombres y mujeres.
'''
'''
# personas=[]
# for n in range(1,101):
#     genero=randint(0,1) #0 para mujeres y el 1 para hombres
#     if (genero ==1):
#         personas.append("H")
#     else:
#         personas.append("M")
'''
# **NOTA:** Puede optimizar el código anterior utilizando compresión de listas.
''' A hacer: 
#¿ Deberá complementar su programa en Python para que cumpla con las siguientes condiciones:
#¿ - Mostrar una opción para generar la lista aleatoria  con datos de los 100 hombres 
#¿ - Mostrar una opción para recuperar la lista del fichero en disco (si existe) o generar una nueva lista.
#¿ - Mostrar con la lista generada o recuperada del disco las siguientes opciones estadísticas:
#¿   - Numero de Hombres
#¿   - Numero de Mujeres
#¿  - Porcentaje de Hombres y Porcentaje de Mujeres
#¿ - (Opcional) Realice la opción para que el resultado de las opciones estadísticas se puedan guardar en un fichero json.
'''

import random
from pymongo import MongoClient
import os, platform

if platform.system() == "Windows":
    os.system("cls")
    print("Estás en Windows")

elif platform.system() == "Darwin" :
    os.system("clear")
    print("Estás en MacOS")

elif platform.system() == "Linux" :
    os.system("clear")
    print("Estás en Linux")


# conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)
db = client['generos']
collection = db['personas']

# opción para generar los datos aleatoriamente y almacenarlos en la base de datos
def generar_y_almacenar():
    generos = random.choices(['H', 'M'], k=100)
    hombres, mujeres, porcentaje_hombres, porcentaje_mujeres = clasificar_generos(generos)
    documento = {
        'generos': generos,
        'hombres': hombres,
        'mujeres': mujeres,
        'porcentaje_hombres': porcentaje_hombres,
        'porcentaje_mujeres': porcentaje_mujeres
    }
    collection.insert_one(documento)
    print('Datos generados y almacenados correctamente.')


# función para clasificar y contar los géneros
def clasificar_generos(generos):
    hombres = generos.count('H')
    mujeres = generos.count('M')
    total = hombres + mujeres
    porcentaje_hombres = hombres / total * 100
    porcentaje_mujeres = mujeres / total * 100
    return hombres, mujeres, porcentaje_hombres, porcentaje_mujeres



# opción para recuperar los datos de la base de datos o generarlos de nuevo y almacenarlos
def recuperar_o_generar():
    documento = collection.find_one()
    if documento is not None:
        print(f'Datos recuperados de la base de datos:\n{documento}')
    else:
        generar_y_almacenar()

# opción para guardar los resultados de las opciones estadísticas en la base de datos
def guardar_resultados(hombres, mujeres, porcentaje_hombres, porcentaje_mujeres):
    documento = {
        'hombres': hombres,
        'mujeres': mujeres,
        'porcentaje_hombres': porcentaje_hombres,
        'porcentaje_mujeres': porcentaje_mujeres
    }
    collection.insert_one(documento)
    print('Resultados guardados correctamente.')

# menú principal del programa
while True:
    opcion = input('Ingrese una opción:\n1. Generar y almacenar datos aleatorios.\n2. Recuperar o generar datos y almacenarlos.\n3. Clasificar y contar los géneros.\n4. Salir.\n')
    if opcion == '1':
        generar_y_almacenar()
    elif opcion == '2':
        recuperar_o_generar()
    elif opcion == '3':
        documento = collection.find_one()
        if documento is None:
            print('No hay datos en la base de datos. Por favor genere o recupere los datos primero.')
        else:
            hombres, mujeres, porcentaje_hombres, porcentaje_mujeres = clasificar_generos(documento['generos'])
            print(f'Hombres: {hombres} ({porcentaje_hombres:.2f}%)')
            print(f'Mujeres: {mujeres} ({porcentaje_mujeres:.2f}%)')
            guardar_resultados(hombres, mujeres, porcentaje_hombres, porcentaje_mujeres)
    elif opcion == '4':
        break
    else:
        print('Opción inválida. Por favor intente de nuevo.') 
