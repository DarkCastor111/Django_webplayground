from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .models import Hilo, Mensaje
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name="dispatch")
class HiloListView(TemplateView):
    template_name = "messenger/hilo_list.html"
'''
¡¡
Podemos acceder a todos los hilos de un user con user.hilos_activos
!!
def HiloList(ListView):
    model = Hilo

    def get_queryset(self):
        qset = super(HiloList, self).get_queryset
        return qset.filter(users=self.request.user)
'''
@method_decorator(login_required, name="dispatch")
class HiloDetailView(DetailView):
    model = Hilo

    def get_object(self):
        hilo = super(HiloDetailView, self).get_object()
        if self.request.user not in hilo.users.all():
            raise Http404()
        return hilo
    
def anadir_mensaje(request, p_pk):
    json_respuesta = {'creada':False}
    if request.user.is_authenticated:
        cnt = request.GET.get('contenido', None)
        if cnt:
            hilo = get_object_or_404(Hilo, pk=p_pk)
            mensaje = Mensaje.objects.create(emisor=request.user, contenido=cnt)
            hilo.mensajes.add(mensaje)
            json_respuesta["creada"] = True
            if len(hilo.mensajes.all()) == 1:
                json_respuesta["primero"] = True
    else:
        raise Http404("Usuario no identificado")

    return JsonResponse(json_respuesta)

@login_required
def iniciar_hilo(request, p_username):
    emisor = request.user
    receptor = get_object_or_404(User, username=p_username)
    hilo = Hilo.objects.find_or_create(emisor,receptor)
    return redirect(reverse_lazy('messenger:hdetail', args=[hilo.pk]))