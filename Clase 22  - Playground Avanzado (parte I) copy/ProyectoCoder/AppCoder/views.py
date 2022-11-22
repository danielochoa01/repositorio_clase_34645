from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Redireccion
from django.urls import reverse_lazy
# Auth
from django.contrib.auth.views import LoginView, LogoutView

#Los decoradores sirven para funciones > vistas basadas en funciones
from django.contrib.auth.decorators import login_required

#ejemplo
# @decorador
# def funcion_a_proteger

#Los mixins sirven para clases > vistas basadas en clases
from django.contrib.auth.mixins import LoginRequiredMixin

#ejemplo
# class ClaseAProteger(MixinParaProteger)

from .models import Curso, Profesor, Avatar
from .forms import CrearCursoForm, CrearProfesorForm, SignUpForm, UserEditForm


# Create your views here.
def mostrar_curso(request):
    curso = Curso(nombre='Python', comision='34635')

    saludo = f'Hola a la todos, este es el curso de {curso.nombre}, con numero de comision: {curso.comision}'

    return HttpResponse(saludo)
    #return render(request, '', {'nombre': curso.nombre, 'comision': curso.comision})

#@login_required
def mostrar_index(request):

    imagenes = Avatar.objects.filter(user=request.user.id)

    return render(request, 'index.html', {'url': imagenes[0].imagen.url})


def mostrar_referencias(request):

    return render(request, 'referencias.html')


def mostrar_repaso(request):

    return render(request, 'repaso.html')


def crear_curso(request):


    if request.method == 'POST':

        formulario = CrearCursoForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            curso = Curso(nombre=formulario_limpio['nombre'], comision=formulario_limpio['comision'])

            curso.save()

            return render(request, 'index.html')

    else:
        formulario = CrearCursoForm()

    return render(request, 'crear_curso.html', {'formulario': formulario})


def crear_profesor(request):

    if request.method == 'POST':

        formulario = CrearProfesorForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            profesor = Profesor(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'], profesion=formulario_limpio['profesion'])

            profesor.save()

            return render(request, 'index.html')

    else:
        formulario = CrearProfesorForm()
    return render(request, 'crear_profesor.html', {'formulario': CrearProfesorForm})


def buscar_comision(request):

    if request.GET.get('comision', False): # -> 12345
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, 'buscar_comision.html', {'cursos': cursos})
    else:
        respuesta = 'No hay datos'
    return render(request, 'buscar_comision.html', {'respuesta': respuesta})


def buscar_profesor(request):

    if request.GET.get('email', False):
        email = request.GET['email']
        profesores = Profesor.objects.filter(email__icontains=email)

        return render(request, 'buscar_profesor.html', {'profesores': profesores})
    else:
        respuesta = 'No hay datos'
    return render(request, 'buscar_profesor.html', {'respuesta': respuesta})


def mostrar_profesores(request):

    profesores = Profesor.objects.all()

    context = {'profesores': profesores}

    return render(request, 'mostrar_profesores.html', context=context)


def eliminar_profesor(request, profesor_id):

    profesor = Profesor.objects.get(id=profesor_id)

    profesor.delete()

    profesores = Profesor.objects.all()

    context = {'profesores': profesores}

    return render(request, 'mostrar_profesores.html', context=context)


def actualizar_profesor(request, profesor_id):

    profesor = Profesor.objects.get(id=profesor_id)

    if request.method == 'POST':

        formulario = CrearProfesorForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            profesor.nombre = formulario_limpio['nombre']
            profesor.apellido = formulario_limpio['apellido']
            profesor.email = formulario_limpio['email']
            profesor.profesion = formulario_limpio['profesion']

            profesor.save()

            return render(request, 'index.html')

    else:
        formulario = CrearProfesorForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
    return render(request, 'actualizar_profesor.html', {'formulario': CrearProfesorForm, 'profesor': profesor})



def editar_usuario(request):

    usuario = request.user

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)

        if usuario_form.is_valid():

            informacion = usuario_form.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, 'index.html')

    else:
        usuario_form = UserEditForm(initial={
            'username': usuario.username,
            'email': usuario.email,
        })

    return render(request, 'AppCoder/admin_update.html', {
        'form': usuario_form,
        'usuario': usuario
    })


class CursoList(LoginRequiredMixin, ListView):

    model = Curso
    template_name = 'AppCoder/cursos_list.html'


class CursoDetailView(DetailView):

    model = Curso
    template_name = 'AppCoder/curso_detalle.html'

class CursoDeleteView(DeleteView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Curso
    success_url = '/cursos_list'


class CursoUpdateView(UpdateView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Curso
    success_url = '/cursos_list'
    fields = ['nombre', 'comision']


class CursoCreateView(LoginRequiredMixin, CreateView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Curso
    success_url = '/cursos_list'
    fields = ['nombre', 'comision']


class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'registro.html'


class AdminLoginView(LoginView):
    template_name = 'login.html'

class AdminLogoutView(LogoutView):
    template_name = 'logout.html'


class AdminUpdateView(UpdateView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Curso
    success_url = '/cursos_list'
    fields = ['nombre', 'comision']


