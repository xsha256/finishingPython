from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():

    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Salario</title>
    </head>
    <body>
        <h1 align="center" style="color:red">Calcular el salario</h1>
        <form method="post" action="/verificar" align="center" style="color:blue">
            <label for="number">Introduce tu salario base:</label>
            <br>
            <input type="number" name="salarioBase" id="salarioBase">
            <br>
            <br>
            <label for="number">Introduce las horas trabajadas:</label>
            <br>
            <input type="number" name="horasTrabajadas" id="horasTrabajadas">
            <br>
            <br>
            <label for="number">Introduce el percentaje de la seguridad social: </label>
            <br>
            <input type="number" name="percentajeSSocial" id="percentajeSSocial">
            <br>
            <br>
            <label for="number">Introduce el percentaje de la impuestos:</label>
            <br>
            <input type="number" name="percentajeImpuestos" id="percentajeImpuestos">
            <br>
            <br>
        <input type="submit" value"Submit">
        </form>
    </body>
    </html>
    """


@app.route('/verificar', methods=['POST'])
def verificar():
    salarioBase = request.form["salarioBase"]
    horasTrabajadas = request.form["horasTrabajadas"]
    percentajeSSocial = request.form["percentajeSSocial"]
    percentajeImpuestos = request.form["percentajeImpuestos"]
    resultado = salario(salarioBase, horasTrabajadas,
                        percentajeSSocial, percentajeImpuestos)
    return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Resultado</title>
    </head>
    <body>
        <h1 align="center" style="color:red">El salario neto: </h1>
        <h3 align="center" style="color:blue">{resultado}</h3>
    </body>
    </html>
        """


def salario(salarioBase, horasTrabajadas, percentajeSSocial, percentajeImpuestos):

    sueldoBruto = int(salarioBase) * int(horasTrabajadas)
    descuentoSS = int((sueldoBruto) * int(percentajeSSocial)) / 100
    descuentoIm = int((sueldoBruto) * int(percentajeImpuestos)) / 100
    sueldoNeto = int(sueldoBruto - descuentoIm - descuentoSS)
    return f"Tu sueldo neto es: {sueldoNeto: .2f}"


if __name__ == "__main__":
    app.run()
