from django import forms


class medicosFormulario(forms.Form):

    nombre = forms.CharField(max_length= 40)
    apellido =  forms.CharField(max_length=40)
    especialidad =  forms.CharField(max_length=40)
    matricula =  forms.IntegerField()

class pacientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    fecha_ingreso = forms.DateField()
    mail = forms.EmailField()

class enfermerosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    turno = forms.CharField(max_length=40)
    n_empleado = forms.IntegerField()

