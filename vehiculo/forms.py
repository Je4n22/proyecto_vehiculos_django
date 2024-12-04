from django import forms
from .models import Vehiculo
from django.contrib.auth.forms import UserCreationForm

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca','modelo','serCar','serMot','categoria','precio']

class formUsuario(UserCreationForm):
    pass