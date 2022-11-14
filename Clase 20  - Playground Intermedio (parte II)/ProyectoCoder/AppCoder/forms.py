from django import forms

class CrearCursoForm(forms.Form):

    nombre = forms.CharField()
    comision = forms.IntegerField()


class CrearProfesorForm(forms.Form):

    nombre = forms.CharField(min_length=5, max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)