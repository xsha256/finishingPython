# Finishing Python

### Instrucciones de instalación:

- Clonar el repositorio:

  - `git clone https://github.com/JonPiniesEcheguren/MiddlePython.git`

- Crear y activar el entorno virtual:

  - Versión Python 3.11.2

  - Windows

    - `python -m venv env`
    - `env\scripts\activate.bat` (Windows command line)
    - `env\scripts\activate.ps1` (Windows PowerShell)

  - MacOs / Linux

    - `python3 -m venv env`

    - `source env/bin/activate`

- Instalar las librerias

  - `pip install -r requirements.txt`

- Instrucciones de ejecución
  - `py main.py`

### Colaboradores:

- Mohamed Amri
- Miguel Aparicio García-Donas

Ejercicios de carácter puramente educativo.

## Los programas presentes en este repositorio fueron creados para resolver los siguientes problemas:

### Ejercicios de Base de Datos:

Elegir uno de los ejercicios de ficheros y utilizar en cambio de ficheros la BBDD (Se puede elegir entre MongoDB o SQL Server).

#### 1 - Lista de hombres y mujeres
####  2 - Lista de personas para por edades.
####  3 - Lista de Personas
####  4 - Temperatura mensual de 20 ciudades


### Condiciones:

Deberá completar su programa en Python para que cumpla con las siguientes condiciones:

- Mostrar una opción para generar los datos de forma aleatoria y almacenarlo en la BBDD.
- Mostrar una opción para recuperar los datos de la BBDD (si existe) o generarlos de nuevo y almacenarlos en la BBDD.
- Realice la opción para que el resultado de las opciones estadísticas se puedan guardar en la BBDD.

### Ejercicios con Flask:

1) Mostrar una página que ponga 6 opciones: (1)

​		Elegir para las 6 opciones 6 de los 20 ejercicios (DNI, Salario, Par o Impar, Celsius, etc)

2) Cuando se pase a la página de la opción, se verá su funcionalidad

   1) Total de paginas HTML dinámicas: 12
      1) Pagina de solicitud de datos
      2) Pagina de resultados
