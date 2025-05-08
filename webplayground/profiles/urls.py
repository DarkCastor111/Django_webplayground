from django.urls import path
from .views import PerfilListView, PerfilDetailView

profiles_patterns = ([
    path('', PerfilListView.as_view(), name='plist'),
    path('<username>/', PerfilDetailView.as_view(), name='pdetail'),
], 'profiles')