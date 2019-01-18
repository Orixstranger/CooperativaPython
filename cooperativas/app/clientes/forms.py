from django import forms
from app.modelo.models import Cliente
from app.modelo.models import Cuenta

from app.modelo.models import Transaccion
from django.utils.translation import gettext as _
from app.modelo.models import Transferencia

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]
        error_messages = {
            'cedula': {
                'required': _(""),
                'unique': _("Esta cedula ya existe"),

            },
            'nombres': {
                'required': _(""),
            },
            'apellidos': {
                'required': _(""),
            },



        }

        labels = {
            "cedula": _("Rule Title"),
        }






class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = [ "tipoCuenta"]


class FormularioTransaccion(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = [  "tipo", "valor", "descripcion"]



class FormularioTransferencia(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ["valor", "descripcion"]


