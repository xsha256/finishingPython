from flask import Flask,request
import random


app = Flask(__name__)
numero = 0
intentos = 0
nalea = random.randint(1,100)
@app.route("/")
def index():
    return """
<!DOCTYPE html>
    <html>
    <head>
        <title>Juego Adivinación</title>
    </head>
    <body>
        <h1>Juego de Adivinación</h1>
        <p>¡Vamos a jugar a un juego!</p>
        <p>Voy a pensar un número del 1 al 100.</p>
        <p>¡A ver si eres capaz de adivinarlo!</p>
        <p>Venga, ¿Cuál es mi número?</p>
        <form method="post" action="/validar">
            <label for="numero">numero:</label>
            <input type="number" name="numero" id="numero" required>
            <br>
            <p>Presione entrar para validar.</p>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """ 

@app.route('/validar', methods=['POST'])
def validar():
    mayormenor = ""
    global intentos
    intentos = intentos + 1
    numero = int(request.form["numero"])
    if nalea != numero:
        if nalea > numero:
            mayormenor = "Es más grande. prueba de nuevo."
        if nalea < numero:
            mayormenor = "Es más pequeño. prueba de nuevo."
        return f"""
<!DOCTYPE html>
    <html>
    <head>
        <title>Juego Adivinación</title>
    </head>
    <body>
        <h1>¡Has Fallado!</h1>
        <p>{mayormenor}</p>
        <p>Llevas {intentos} intentos.</p>
        <form method="post" action="/validar">
            <label for="numero">numero:</label>
            <input type="number" name="numero" id="numero" required>
            <br>
            <p>Presione entrar para validar.</p>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """ 
    else:
        return f"""
    <!DOCTYPE html>
        <html>
        <head>
            <title>Juego Adivinación</title>
        </head>
        <body>
            <h1>¡HAS ACERTADO!</h1>
            <p>El número era {nalea}</p>
            <p>Has necesitado {intentos} intentos para acertarlo.</p>
        </body>
        </html>
            """            
if __name__ == "__main__":
    app.run()