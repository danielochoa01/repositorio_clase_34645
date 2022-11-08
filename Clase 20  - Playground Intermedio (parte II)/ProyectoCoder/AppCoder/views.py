from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.
def mostrar_curso(request):
    curso = Curso(nombre='Python', comision='34635')

    saludo = f'Hola a la todos, este es el curso de {curso.nombre}, con numero de comision: {curso.comision}'

    return HttpResponse(saludo)
    #return render(request, '', {'nombre': curso.nombre, 'comision': curso.comision})

def mostrar_index(request):

    return render(request, 'index.html')


def mostrar_referencias(request):

    return render(request, 'referencias.html')


def mostrar_repaso(request):

    return render(request, 'repaso.html')