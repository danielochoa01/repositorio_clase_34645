from django.http import HttpResponse
from django.shortcuts import render
import datetime


def saludo(request):
    return HttpResponse('hola esta clase es horrible')


def segunda_vista(request):
    return HttpResponse('les parecio facil?')

def dia_actual(request):

    dia = datetime.datetime.now()

    return HttpResponse(f'La fecha de hoy es: {dia}')


def saludo_personalizado(request, nombre):

    return HttpResponse(f'Hola {nombre}')

def mostrar_html(request):
    return render(request, 'hola.html')

def saludo_ing(request):

    return render(request, 'inge.html', {'nombre': 'Franco', 'lista': [1,2,3,4]})