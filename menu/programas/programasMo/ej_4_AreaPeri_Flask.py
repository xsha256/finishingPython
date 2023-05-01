from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():

    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Area Perimetro</title>
    </head>
    <body>
        <h1>Calcular el Area y el Perimetro</h1>
        <form method="post" action="/verificar">
            <label for="number">Introduce el radio:</label>
            <input type="number" name="radio" id="radio">
            <br>
        <input type="submit" value"Submit">
        </form>
    </body>
    </html>
    """


@app.route('/verificar', methods=['POST'])
def verificar():
    radio = request.form["radio"]

    resultado = CalcularAreaPer(radio)
    return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Resultado</title>
    </head>
    <body>
        <h1>El area y el perimetro? </h1>
        <p>{resultado}</p>
    </body>
    </html>
        """


def CalcularAreaPer(radio):
    #! π = 3.14159
    pi = 3.14159
    area = 0
    perimetro = 0

    if str(radio).isnumeric():

        #! Área = π × radio²
        area = int(pi) * int(radio) ** 2

        #! Perímetro = 2 × π × radio
        perimetro = 2 * pi * int(radio)

        return f"""
  El área es: {area:.2f}.
  El perímetro es: {perimetro:.2f}"""

    else:
        return ("Radio inválido")


if __name__ == "__main__":
    app.run()
