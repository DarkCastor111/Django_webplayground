from django.urls import path
from .views import HiloListView, HiloDetailView, anadir_mensaje, iniciar_hilo

messenger_patterns = ([
    path('', HiloListView.as_view(), name='hlist'),
    path('hilo/<int:pk>/', HiloDetailView.as_view(), name='hdetail'),
    path('hilo/<int:p_pk>/anadir', anadir_mensaje, name='hadd'),
    path('hilo/start/<p_username>', iniciar_hilo, name='hiniciar'),
], 'messenger')
