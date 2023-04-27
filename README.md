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

## Ejercicios sobre JSON

Dados los siguientes JSON, deberá crear un programa en python, que pida la información por teclado, conforme un objeto Python y al final convierta el objeto conformado al JSON correspondiente:

### Programa 1: Información sobre un usuario:

El JSON generado deberá ser.

```
{"nombre": "Juan", "edad": 30, "email": "juan@acme.com", "trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}
```

### Programa 2: Transacción financiera:

El JSON generado deberá ser.

```
{"id": 123456789, "fechayhora": "2023-04-18T12:30:00Z", "monto": 500.25, "tipo": "compra", "producto": {"nombre": "Smartphone", "precio": 450.00, "descripcion": "Un teléfono inteligente de última generación"}}
```

### Programa 3: Información medica de paciente:

El JSON generado deberá ser:

```
{"nombre": "Pedro", "apellido": "Pérez", "edad": 45, "peso": 80.5, "altura": 1.75, "historial_medico": {"alergias": ["penicilina", "mariscos"], "problemas_cardiacos": false, "medicamentos": [{"nombre": "Ibuprofeno", "dosis": "200mg"}, {"nombre": "Paracetamol", "dosis": "500mg"}]}, "ultima_revision": "2022-10-01", "proximo_turno": "2023-05-15"}
```

**NOTA: **Para comprobar los programas anteriores, cree un programa en python, que pida un JSON como texto y lo convierta en un objeto Python y lo muestre por pantalla.

## Ejercicios básicos de clases

### Programa 1:

Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) y `grosor` (entero). El constructor debe inicializar ambos atributos con valores por defecto. Agregar un método `escribir` que imprima por pantalla la frase "Escribiendo con un lapiz de [color] y grosor [grosor]". Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.

### Programa 2:

Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) y `color` (cadena de caracteres). El constructor debe recibir ambos atributos como argumentos e inicializarlos. Agregar un método `mostrar_informacion` que imprima por pantalla el nombre y color de la flor. Crear dos objetos de la clase `Flor` e invocar el método `mostrar_informacion` para ambos.

### Programa 3:

Dada la siguiente lista de productos.

```
productos_lista = [
    {"nombre": "Leche", "precio": 2.50, "stock": 10},
    {"nombre": "Huevos", "precio": 1.50, "stock": 20},
    {"nombre": "Pan", "precio": 1.00, "stock": 15}
]
```

Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de productos.

### Programa 4:

Dada la siguiente lista de alumnos.

```
alumnos_lista = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
    {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
    {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]} ]
```

Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.
La clase deberá tener un método que incorpore el promedio de las notas del alumno.
