from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    escuela = "UTL!!!"
    alumnos = ["Simón", "Alec", "Ulises"]
    return render_template("index.html", escuela=escuela, alumnos=alumnos)


@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")


@app.route("/maestros")
def maestros():
    return render_template("maestros.html")


@app.route("/hola")
def hola():
    return '<p><h1>Hola que hace :)<br>Mundo</h1></p>'


@app.route("/user/<string:name>")
def user(name):
    return "<h1>Hola "+name+"</h1>"


@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es: {n}"


@app.route("/user/<int:id>/<string:name>")
def fun(id, name):
    return f"El usuario es: {name}, con id: {id}"


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f'El resultado de la suma del numero {n1} con {n2} es: {n1+n2}'


@app.route("/default")
@app.route("/default/<string:ab>")
def func1(ab="UTL"):
    return f"El valor es {ab}"


@app.route("/multiplicar", methods=["GET", "POST"])
def mult():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return f'<h1>La multiplicación es: {str(int(num1) * int(num2))} </h1>'
    else:
        return '''
        <form action="/multiplicar" method="POST">
            <label> N1:</label>
            <input type="text" name="n1"/>
            <label> N2:</label>
            <input type="text" name="n2"/>
            <input type="submit"/>
        </form>
    '''


@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return f'<h1>La multiplicación es: {str(int(num1) * int(num2))} </h1>'


@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")


@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")


if __name__ == '__main__':
    app.run(debug=True)
