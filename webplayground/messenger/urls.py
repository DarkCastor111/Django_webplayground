from django.urls import path
from .views import HiloListView, HiloDetailView

messenger_patterns = ([
    path('', HiloListView.as_view(), name='hlist'),
    path('hilo/<int:pk>/', HiloDetailView.as_view(), name='hdetail'),
], 'messenger')
