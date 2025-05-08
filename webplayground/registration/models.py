from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instancia, nombre_fichero):
    antigua_instancia = Profile.objects.get(pk=instancia.pk)
    antigua_instancia.avatar.delete()
    return 'profiles/' + nombre_fichero

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    class Meta():
        ordering = ['-user__pk']

@receiver(post_save, sender=User)
def asegurar_existencia_perfil(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Creación Usuario y su Perfil enlazado")