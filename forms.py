from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators


class UsersForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message='El campo nombre es requerido'),
        validators.length(min=4, max=10, message='Ingrese nombre valido')])

    aPaterno = StringField("APaterno", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingrese apellido paterno valido')])

    aMaterno = StringField("AMaterno", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingrese apellido materno valido')])

    edad = IntegerField("Edad", [
        validators.DataRequired(message='El campo es requerido'),
        validators.number_range(min=1, max=20, message='valor no valido')])

    correo = EmailField("Correo", [
        validators.Email(message='Ingrese un correo valido')
    ])
