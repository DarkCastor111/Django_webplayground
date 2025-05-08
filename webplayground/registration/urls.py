from django.urls import path
from .views import AltaView, PerfilUpdateView

urlpatterns = [
    path('signup/', AltaView.as_view(), name='signup'),
    path('profile/', PerfilUpdateView.as_view(), name='profile'),

]