from flask import Flask,request
from programas.programasMig.anagramas import anagramas

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
        <h1>Introduzca dos frases para determinar si son anagramas.</h1>
        <form method="post" action="/validar">
            <label for="textoa">Introduzca cadena de texto A:</label>
            <input type="text" name="textoa" id="textoa" required>
            <br>
            <label for="textob">Introduzca cadena de texto B:</label>
            <input type="text" name="textob" id="textob" required>
            <br>
            <p>Presione entrar para ordenar.</p>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     textoaPagWeb= request.form["textoa"]
     textobPagWeb= request.form["textoa"]
     resultado=anagramas(textoaPagWeb, textobPagWeb)
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