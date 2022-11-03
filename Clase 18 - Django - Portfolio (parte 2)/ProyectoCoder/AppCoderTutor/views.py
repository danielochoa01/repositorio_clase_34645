from django.shortcuts import render
from .models import Curso, Repaso

# Create your views here.
def mostrar_curso_html(request):

    curso1 = Curso(nombre='Python', comision='34635')
    curso2 = Curso(nombre='Data Science', comision='16310')
    curso3 = Curso(nombre='Django', comision='59145')
    repaso = Repaso(clase=18, tema_a_repasar='Vistas')

    return render(request, 'mostrar_curso.html', {'cursos': [curso1, curso2, curso3], 'repaso': repaso})