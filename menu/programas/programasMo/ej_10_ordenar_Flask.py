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
                        top: 50%;
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
            <h1 class="center-middle2" align="center" style="color:red">Ordenar cadena de palabras</h1>
            <form method="post" action="/verificar"  class="center-middle" align="center" align="middle" style="color:blue">
                <label for="text">Introduce la primera cadena:</label>
                <br>
                <input type="text" name="pala1" id="pala1">
                <br>
                <br>
                <label for="text">Introduce la segunda cadena:</label>
                <br>
                <input type="text" name="pala2" id="pala2">
                <br>
                <br>
                <label for="text">Introduce la tercera cadena:</label>
                <br>
                <input type="text" name="pala3" id="pala3">
                <br>
                <br>
                <label for="text">Introduce la cuarta cadena:</label>
                <br>
                <input type="text" name="pala4" id="pala4">
                <br>
                <br>
            <input type="submit" value"Submit">
            </form>
        </body>
        </html>
        """

@app.route('/verificar', methods=['POST'])
def verificar():
    palab1 = request.form["pala1"]
    palab2 = request.form["pala2"]
    palab3 = request.form["pala3"]
    palab4 = request.form["pala4"]
    resultado = Ordenar(palab1, palab2, palab3, palab4)
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


def Ordenar(palab1, palab2, palab3, palab4):
    lista = [palab1, palab2, palab3, palab4]
    lista.sort()
    pal1, pal2, pal3, pal4 = lista

    return f"La cadena ordenada:  <br> {pal1} <br> {pal2} <br> {pal3}  <br> {pal4}"



if __name__ == "__main__":
    app.run()
