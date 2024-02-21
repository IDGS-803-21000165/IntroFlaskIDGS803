from flask import Flask, render_template, request, flash, Response, g, redirect
from flask_wtf.csrf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key = "esta es la clave secreta"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    g.nombre = 'Alec'
    if 'Simón' not in g.nombre and request.endpoint not in ['index']:
        return redirect('index')
    # print('before_request')


@app.after_request
def after_request(response):
    print('after_request')
    return response


@app.route("/index")
def index():
    escuela = "UTL!!!"
    alumnos = ["Simón", "Alec", "Ulises"]
    return render_template("index.html", escuela=escuela, alumnos=alumnos)


@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    print('Dentro de alumnos')
    print(f'Hola: {g.nombre}')
    alum_form = forms.UsersForm(request.form)
    nom = ''
    apa = ''
    ama = ''
    edad = 0
    correo = ''
    if request.method == 'POST' and alum_form.validate():
        nom = alum_form.nombre.data
        apa = alum_form.aPaterno.data
        ama = alum_form.aMaterno.data
        edad = alum_form.edad.data
        correo = alum_form.correo.data
        mensaje = f'Bienvenido {nom}'
        flash(mensaje)

        print(
            f'Nombre: {nom}, aPaterno: {apa}, aMaterno: {ama}, Edad: {edad}, Correo: {correo}')

    return render_template("alumnos.html", form=alum_form, nom=nom, apa=apa, ama=ama, edad=edad, correo=correo)


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
