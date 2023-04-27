from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():

    return """
    <!DOCTYPE html>
        <html>
        <head>
            <title>Salario</title>
                <style>
                    .center-middle {
                        position: absolute;
                        top: 35%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                                            }
                    .center-middle2{
                        position: absolute;
                        top: 27%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                    }
            </style>
        </head>
        <body>
            <h1 class="center-middle2" align="center" style="color:red">Una cadena de texto es palíndromo o no</h1>
            <form method="post" action="/verificar"  class="center-middle" align="center" align="middle" style="color:blue">
                <label for="text">Introduce un palabra/frase:</label>
                <br>
                <input type="text" name="pala" id="pala">
            <input type="submit" value"Submit">
            </form>
        </body>
        </html>
        """


@app.route('/verificar', methods=['POST'])
def verificar():
    pala = request.form["pala"]
    resultado = palindromo(pala)
    return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Resultado</title>
            <style>
                    .center-middle {{
                            position: absolute;
                            top: 35%;
                            left: 50%;
                            transform: translate(-50%, -50%);
                                                }}
                        .center-middle2 {{
                            position: absolute;
                            top: 30%;
                            left: 50%;
                            transform: translate(-50%, -50%);
                    }}
            </style>
    </head>
    <body>
        <h1 class="center-middle2" align="center" style="color:red">El resultado: </h1>
        <h3 class="center-middle" align="center" style="color:blue">{resultado}</h3>
    </body>
    </html>
        """


def palindromo(cadena):
    #! lower(): para convertir a minúsculas
    #! replace(): para eliminar espacios en blanco
    cadenaOri = cadena.lower().replace(" ", "")

    #! invertir la cadena
    cadenaReversa = cadenaOri[::-1]

    if cadenaOri == cadenaReversa:
        return f"La cadena {cadenaOri} es un palíndromo"
    else:
        return f"La cadena {cadenaOri} no es un palíndromo"


if __name__ == "__main__":
    app.run()
