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
            <h1 class="center-middle2" align="center" style="color:red">Buscar el número mayor y el número menor</h1>
            <form method="post" action="/verificar"  class="center-middle" align="center" align="middle" style="color:blue">
                <label for="number">Introduce un numero:</label>
                <br>
                <input type="number" name="numMaMe" id="numMaMe">
                <br>
                <br>
                <label for="number">Introduce un numero:</label>
                <br>
                <input type="number" name="numMaMe2" id="numMaMe2">
                <br>
                <br>
                <label for="number">Introduce un numero:</label>
                <br>
                <input type="number" name="numMaMe3" id="numMaMe3">
                <br>
                <br>
                <label for="number">Introduce un numero:</label>
                <br>
                <input type="number" name="numMaMe4" id="numMaMe4">
                <br>
                <br>
            <input type="submit" value"Submit">
            </form>
        </body>
        </html>
        """

@app.route('/verificar', methods=['POST'])
def verificar():
    numero1 = request.form["numMaMe"]
    numero2 = request.form["numMaMe2"]
    numero3 = request.form["numMaMe3"]
    numero4 = request.form["numMaMe4"]
    resultado = CalcularMayMen(numero1, numero2,
                        numero3, numero4)
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

def CalcularMayMen(numero1, numero2, numero3, numero4):
        numeros = [numero1, numero2, numero3, numero4]
        mayor = float("-inf")
        menor =  float("inf")

        for numero in numeros:
                if int(numero) >  mayor:   
                        mayor = int(numero) 
                if int(numero) < menor:
                        menor = int(numero)

        return f''' El numero mayor es: {mayor} <br><br> El numero menor es: {menor} '''


if __name__ == "__main__":
    app.run()
