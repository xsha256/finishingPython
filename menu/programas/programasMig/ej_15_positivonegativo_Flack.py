from flask import Flask,request
from positivonegativo import mayormenor0

app = Flask(__name__)

@app.route("/")
def index():
    return  """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular si un número en mayor o menor que 0</title>
    </head>
    <body>
        <h1>Numero a comprobar</h1>
        <form method="post" action="/validar">
            <label for="numero">Número:</label>
            <input type="number" step="any" name="numero" id="numero">
            <br>
            <p>Presione entrar para validar.</p>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     numeroPagWeb= request.form["numero"]
     resultado=mayormenor0(numeroPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular si un número en mayor o menor que 0</title>
    </head>
    <body>
        <h1>Calculo realizado</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

if __name__ == "__main__":
    app.run()