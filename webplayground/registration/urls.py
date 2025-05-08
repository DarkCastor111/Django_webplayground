from django.urls import path
from .views import AltaView, PerfilUpdateView, PerfilEmailView

urlpatterns = [
    path('signup/', AltaView.as_view(), name='signup'),
    path('profile/', PerfilUpdateView.as_view(), name='profile'),
    path('profile/email/', PerfilEmailView.as_view(), name='profile_email'),

]