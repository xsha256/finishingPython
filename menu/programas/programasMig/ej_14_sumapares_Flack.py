from flask import Flask,request
from sumapares import sumapares

app = Flask(__name__)

@app.route("/")
def index():
    return  """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Sumar los elementos pares de una lista de números</title>
    </head>
    <body>
        <h1>Numeros a comprobar</h1>
        <form method="post" action="/validar">
            <label for="texto">texto:</label>
            <input type="text" name="texto" id="texto">
            <br>
            <p>Presione entrar para validar.</p>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     textoPagWeb= request.form["texto"]
     resultado=sumapares(textoPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Sumar los elementos pares de una lista de numeros</title>
    </head>
    <body>
        <h1>Cuenta procesada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

if __name__ == "__main__":
    app.run()