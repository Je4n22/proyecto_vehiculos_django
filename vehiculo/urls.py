from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar', views.listar, name='listar'),
    path('crear', views.crear, name='crear'),
    path('form_insertar', views.formInsertar, name='form_insertar'),
    path('form_registrar', views.formRegistrar, name='form_registrar'),
    path('reg_exitoso', views.formExitoso, name='reg_exitoso'),
]
