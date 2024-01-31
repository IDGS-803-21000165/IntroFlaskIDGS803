from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField


class UsersForm(Form):
    nombre = StringField("Nombre")
    aPaterno = StringField("APaterno")
    aMaterno = StringField("AMaterno")
    edad = IntegerField("Edad")
    correo = EmailField("Correo")
