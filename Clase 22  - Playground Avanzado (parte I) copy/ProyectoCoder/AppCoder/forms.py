from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CrearCursoForm(forms.Form):

    nombre = forms.CharField()
    comision = forms.IntegerField()


class CrearProfesorForm(forms.Form):

    nombre = forms.CharField(min_length=5, max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]