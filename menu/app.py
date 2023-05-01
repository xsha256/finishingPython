
from flask import Flask, request, render_template, redirect
import os
import random
from programas.programasMig.anagramas import anagramas
from programas.programasMig.capicua import capicua
from programas.programasMo.ej_4_AreaPeri_Flask import CalcularAreaPer
from programas.programasMo.ej_6_celAFah_Flask import celAfah
from programas.programasMo.ej_7_Par_Impar_Flask import parImpar

app = Flask(__name__, static_folder='static')

os.system('clear')

numero = 0
intentos = 0
nalea = random.randint(1, 100)


@app.route('/')
def index():
    return render_template('index.html')
    app = Flask(__name__)


@app.route('/juego')
def juego():
    return render_template('juego1.html')


@app.route('/juego/validar', methods=['POST'])
def validarJuego():
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
          <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <div class="container">
        <form method="post" action="/juego/validar">
        <h2>¡Has Fallado!</h2>
        <p>{nalea}</p>
        <p>{mayormenor}</p>
        <p>Llevas {intentos} intentos.</p>
        <div class="center">
        <label for="numero">numero:</label><br>
        <input type="number" name="numero" id="numero" required>
        </div>
        <p>Presione entrar para validar.</p>
        <input type="submit" value="Entrar">

        <input type="button" value="Menú" onclick="location.href='/'" />
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
            <link rel="stylesheet" href="/static/css/style.css">
        </head>
        <body>
        <div class="container">
        <form method="post" action="/juego/validar">
            <h2>¡HAS ACERTADO!</h2>
            <p>El número era {nalea}</p>
            <p>Has necesitado {intentos} intentos para acertarlo.</p>
            
            <input type="button" value="Menú" onclick="location.href='/'" />
        </form>
        </body>
        </html>
            """


@app.route('/anagrama')
def anagrama():
    return render_template('anagrama1.html')


@app.route('/anagrama/validar', methods=['POST'])
def validarAna():
    textoPagWeb = request.form["texto"]
    resultado = anagramas(textoPagWeb)
    return render_template('anagrama2.html', resultado=resultado)


@app.route('/areaperi')
def areaperi():
    return render_template('areaPeri1.html')


@app.route('/areaperi/validar', methods=['POST'])
def validarAreaperi():
    radio = request.form["radio"]
    resultado = CalcularAreaPer(radio)
    return render_template('areaPeri2.html', resultado=resultado)


@app.route('/celFah')
def celFah():
    return render_template('celFah1.html')


@app.route('/celFah/validar', methods=['POST'])
def validarCelFah():
    grado = request.form["grado"]
    resultado = celAfah(grado)
    return render_template('celFah2.html', resultado=resultado)


@app.route('/parImpar')
def parImp():
    return render_template('parImpar1.html')


@app.route('/parImpar/validar', methods=['POST'])
def validarParImp():
    numero = request.form["num"]
    resultado = parImpar(numero)
    return render_template('parImpar2.html', resultado=resultado)

@app.route('/capicua')
def capi():
    return render_template('capicua1.html')


@app.route('/capicua/validar', methods=['POST'])
def cvalidarCapi():
    numeroPagWeb= request.form["numero"]
    resultado=capicua(numeroPagWeb)
    return render_template('capicua2.html', resultado=resultado)

if __name__ == "__main__":
    app.run()
