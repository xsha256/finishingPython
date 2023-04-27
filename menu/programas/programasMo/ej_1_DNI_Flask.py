from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Validar DNI</title>
    </head>
    <body>
        <h1>Validar DNI</h1>
        <form method="post" action="/validar">
            <label for="numero">Número:</label>
            <input type="number" name="dni" id="dni">
            <br>
            <label for="letra">Letra:</label>
            <input type="text" name="letra" id="letra" maxlength="1">
            <br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     letraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
     dniPagWeb= request.form["dni"]
     letPagWeb= request.form["letra"]
     resultado=LetraDNI(dniPagWeb,letPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Validar DNI</title>
    </head>
    <body>
        <h1>Validacion realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

def LetraDNI(numero,letra):
    letraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(str(numero)) == 8 and str(numero).isnumeric():
        resto = int(numero) % 23
        if letra == letraDNI[resto]:
            return f"La letra del DNI introducido es: {letraDNI[resto]}, es un DNI Válido"
        else:
            return f"la letra {letra} no corresponde al dni: {numero}"
    else:
        return "DNI inválido"


if __name__ == "main":
    numero=input("Entre el número del DNI:")
    letra =input("Entre la letra del DNI:")
    LetraDNI(numero, letra)

if __name__ == "main":
    app.run()
