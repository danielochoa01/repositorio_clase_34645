"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('mostrar_curso/', views.mostrar_curso, name='Mostrar'),
    path('', views.mostrar_index, name='Home'),
    path('mostrar_referencias/', views.mostrar_referencias, name='Referencias'),
    path('mostrar_repaso/', views.mostrar_repaso, name='Repaso'),
    path('crear_curso/', views.crear_curso, name='Crear Curso'),
    path('crear_profesor/', views.crear_profesor, name='Crear Profesor'),
    path('buscar_comision/', views.buscar_comision, name='Buscar Comision'),
    path('buscar_profesor/', views.buscar_profesor, name='Buscar Profesor'),
    path('mostrar_profesores/', views.mostrar_profesores, name='Mostrar Profesores'),
    path('eliminar_profesor/<profesor_id>', views.eliminar_profesor, name='Eliminar Profesor'),
    path('actualizar_profesor/<profesor_id>', views.actualizar_profesor, name='Actualizar Profesor'),
    path('cursos_list/', views.CursoList.as_view(), name='List'),
    path('curso_detail/<pk>', views.CursoDetailView.as_view(), name='Detail'),
    path('curso_confirm_delete/<pk>', views.CursoDeleteView.as_view(), name='Delete'),
    path('curso_edit/<pk>', views.CursoUpdateView.as_view(), name='Update'),
    path('curso_form/', views.CursoCreateView.as_view(), name='Create'),
    path('signup/', views.SignUpView.as_view(), name='Sign Up'),
    path('login/', views.AdminLoginView.as_view(), name='Login'),
    path('logout/', views.AdminLogoutView.as_view(), name='Logout'),
    path('editar_usuario/', views.editar_usuario, name='Editar Usuario'),
]
