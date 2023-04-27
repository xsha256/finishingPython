from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Número Par o Impar</title>
    </head>
    <body>
        <h1>Número par o impar</h1>
        <form method="post" action="/verificar">
            <label for="number">Intoduce un número:</label>
            <input type="number" name="num" id="num">
            <br>
        <input type="submit" value"Submit">
        </form>
    </body>
    </html>
    """


@app.route('/verificar', methods=['POST'])
def verificar():
    numPagWeb = request.form["num"]
    resultado = parImpar(numPagWeb)
    return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Resultado</title>
    </head>
    <body>
        <h1>Es par o impar? </h1>
        <p>El número {resultado}</p>
    </body>
    </html>
        """


def parImpar(num):
    num = int(num)
    if num%2 == 0:
        return(f"{num} es par")
    else:
        
        return(f"{num} es impar")

if __name__ == "__main__":
    app.run()






