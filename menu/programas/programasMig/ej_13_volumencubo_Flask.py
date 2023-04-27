from flask import Flask,request
from volumencubo import volumencubo

app = Flask(__name__)

@app.route("/")
def index():
    return  """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Determinar el volumen y Area de un Cubo</title>
    </head>
    <body>
        <h1>Valor del lado del cubo</h1>
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
     resultado=volumencubo(numeroPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Determinar el volumen y Area de un Cubo</title>
    </head>
    <body>
        <h1>Calculos realizados</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

if __name__ == "__main__":
    app.run()