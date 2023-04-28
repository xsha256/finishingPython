from flask import Flask,request
from medialista import medialista

app = Flask(__name__)

@app.route("/")
def index():
    return  """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular media</title>
    </head>
    <body>
        <h1>Numeros para hacer la media separados por coma:</h1>
        <form method="post" action="/validar">
            <label for="texto">texto:</label>
            <input type="text" name="texto" id="texto" required>
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
     resultado=medialista(textoPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular media</title>
    </head>
    <body>
        <h1>Calculo realizado</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

if __name__ == "__main__":
    app.run()