from django.db.models.signals import post_save
from django.contrib.auth.models import User, Permission
from django.dispatch import receiver

@receiver(post_save, sender=User)
def asignar_permisos(sender, instance, created, **kwargs):
    if created:
        # Permisos que deseas asignar automáticamente
        permisos = Permission.objects.filter(codename__in=['listar_vehiculos'])  # Ajusta según tus permisos
        instance.user_permissions.add(*permisos)

