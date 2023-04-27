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
            <h1 class="center-middle2" align="center" style="color:red">Convertir de Celius a Fahrenheit</h1>
            <form method="post" action="/verificar"  class="center-middle" align="center" align="middle" style="color:blue">
                <label for="number">Introduce un grado Celsius:</label>
                <br>
                <input type="number" name="grado" id="grado">
            <input type="submit" value"Submit">
            </form>
        </body>
        </html>
        """

@app.route('/verificar', methods=['POST'])
def verificar():
    grado = request.form["grado"]
    resultado = celAfah(grado)
    return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Resultado</title>
            <style>
                    .center-middle {{
                            position: absolute;
                            top: 40%;
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


def celAfah(cel):
    fah = int(cel) * 1.8 + 32
    return f"{cel} Celsius en Fahrenheit = {fah}"


if __name__ == "__main__":
    app.run()
