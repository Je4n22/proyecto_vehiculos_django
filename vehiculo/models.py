from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    serCar = models.CharField(max_length=50, verbose_name='Serial Carroceria')
    serMot = models.CharField(max_length=50, verbose_name='Serial Motor')
    categoria = models.CharField(max_length=20, verbose_name='Categoria')
    precio = models.IntegerField(verbose_name='Precio')
    fec_cre = models.DateTimeField(auto_now_add=True)
    fech_mod = models.DateTimeField(auto_now=True)
    conPrecio = models.CharField(null=True, max_length=50, verbose_name='Condicion de Precio')
    class Meta: 
        permissions = [ 
            ("listar_vehiculos", "Puede Listar Vehiculos"), 
            ("agregar_vehiculos", "Puede Agregar Vehiculos"), 
        ]

    def __str__(self):
        return  f'Marca {self.marca}, Modelo {self.modelo}, Serie Carroceria {self.serCar}'
    