from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_emision = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['fecha_emision']

class HiloManager(models.Manager):
    def find(self, usu1, usu2):
        queryset_resultado = self.filter(users=usu1).filter(users=usu2)
        if len(queryset_resultado) > 0:
            return queryset_resultado[0]
        return None
    
    def find_or_create(self, usu1, usu2):
        hilo_encontrado = self.find(usu1, usu2)
        if hilo_encontrado:
            return hilo_encontrado
        else:
            hilo_creado = Hilo.objects.create()
            hilo_creado.users.add(usu1, usu2)

            return hilo_creado

class Hilo(models.Model):
    users = models.ManyToManyField(User, related_name='hilos_activos')
    mensajes = models.ManyToManyField(Mensaje)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    objects = HiloManager()

    class Meta:
        ordering = ['-fecha_modificacion']

def mensajes_changed(sender, **kwargs):
    # Impedir que un usuario externo añade un mensaje a un hilo
    instancia = kwargs.pop('instance', None)
    accion = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    print(instancia, accion, pk_set)

    false_pk_set = set()
    if accion == "pre_add":
        for msj_pk in pk_set:
            msj = Mensaje.objects.get(pk=msj_pk)
            if msj.emisor not in instancia.users.all():
                print(f'{msj.emisor} no forma parte del hilo -> mensaje borado')
                false_pk_set.add(msj_pk)
    # Borrar los mensajes de false_pk_set de pk_set
    pk_set.difference_update(false_pk_set)

    # Forzar la actualizacion del m2m
    # Útil para actualizar la fecha_modificacion del Hilo
    instancia.save()

m2m_changed.connect(mensajes_changed, sender=Hilo.mensajes.through)
