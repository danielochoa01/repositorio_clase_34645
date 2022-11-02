from django.shortcuts import render
from .models import Curso

# Create your views here.
def mostrar_curso_html(request):

    curso1 = Curso(nombre='Python', comision='34635')
    curso2 = Curso(nombre='Python', comision='34635')
    curso3 = Curso(nombre='Python', comision='34635')

    return render(request, 'mostrar_curso.html', {'objetos': [curso1, curso2, curso3]})