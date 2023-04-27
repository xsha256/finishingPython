from flask import Flask,request
from capicua import capicua

app = Flask(__name__)

@app.route("/")
def index():
    return  """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Determinar número primo</title>
    </head>
    <body>
        <h1>Numero a determinar su condicion de primo</h1>
        <form method="post" action="/validar">
            <label for="numero">Número:</label>
            <input type="number" name="numero" id="numero">
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
     resultado=capicua(numeroPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Determinar número primo</title>
    </head>
    <body>
        <h1>Detección realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

if __name__ == "__main__":
    app.run()