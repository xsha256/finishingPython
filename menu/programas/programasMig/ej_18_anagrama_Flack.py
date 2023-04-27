from flask import Flask,request
from anagramas import anagramas

app = Flask(__name__)

@app.route("/")
def index():
    return  """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Frases Anagrama</title>
    </head>
    <body>
        <h1>Introduzca dos frases separadas por un punto para determinar si son anagramas.</h1>
        <form method="post" action="/validar">
            <label for="texto">text:</label>
            <input type="text" name="texto" id="texto">
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
     resultado=anagramas(textoPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Frases Anagrama</title>
    </head>
    <body>
        <h1>Comprobación realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

if __name__ == "__main__":
    app.run()