from django.shortcuts import render
from .models import Repaso
# Create your views here.

def repaso(request):

    repaso1 = Repaso('Vistas', 18)
    repaso2 = Repaso('Creacion de proyecto', 17)

    return render(request, 'repaso.html', {'tema_a_repasar': repaso1.tema_a_repasar, 'clase': repaso1.clase})
