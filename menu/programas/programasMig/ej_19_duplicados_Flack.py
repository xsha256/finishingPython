from flask import Flask,request
from duplicados import duplicados

app = Flask(__name__)

@app.route("/")
def index():
    return  """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Lista de numeros sin duplicados</title>
    </head>
    <body>
        <h1>Introduzca una lista de números para obtener una nueva lista sin duplicados.</h1>
        <form method="post" action="/validar">
            <label for="texto">text:</label>
            <input type="text" name="texto" id="texto" required>
            <br>
            <p>Presione entrar para ordenar.</p>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     textoPagWeb= request.form["texto"]
     resultado=duplicados(textoPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Lista de numeros sin duplicados</title>
    </head>
    <body>
        <h1>Calculos realizados</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

if __name__ == "__main__":
    app.run()