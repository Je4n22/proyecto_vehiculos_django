from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vehiculo
from .forms import VehiculoForm, formUsuario
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate


# Create your views here.

@login_required
def index(request):
    return render(request, 'vehiculos/index.html')

@login_required
def listar(request):
    vehiculos = Vehiculo.objects.all()   
    return render(request, 'vehiculos/listar.html', {'vehiculos': vehiculos})

@permission_required('vehiculo.agregar_vehiculos', raise_exception=True) 
def formInsertar(request):
    return render(request, 'vehiculos/form_insertar.html')

@permission_required('vehiculo.agregar_vehiculos', raise_exception=True) 
def crear(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        ser_car = request.POST['ser_car']
        ser_mot = request.POST['ser_mot']
        categoria = request.POST['categoria']
        precio = request.POST['precio']
        if 0 < int(precio) <= 10000:
            conPrecio = 'Bajo'
        elif 10000 < int(precio) <= 30000:
            conPrecio = 'Medio'
        elif int(precio) > 30000:
            conPrecio = 'Alto'
        vehiculo = Vehiculo(marca=marca, modelo=modelo, serCar=ser_car, serMot=ser_mot, categoria=categoria, precio=precio, conPrecio=conPrecio)
        vehiculo.save()
        datos = { 'er' : 'Registro Realizado Correctamente!' }
        return render(request, 'vehiculos/form_insertar.html', datos)
    else:
        datos = { 'er2' : 'Presionar botón para guardar datos!'}
        return render(request, 'vehiculos/form_insertar.html', datos)
    
def formRegistrar(request):
    data = {
        'form': formUsuario()
    }
    if request.method == 'POST':
        formulario = formUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=usuario, password=password)
            login(request, user)
            return redirect(to='reg_exitoso')
    return render(request, 'registration/form_registrar.html', data)

@login_required
def formExitoso(request):
    return render(request, 'registration/reg_exitoso.html')
