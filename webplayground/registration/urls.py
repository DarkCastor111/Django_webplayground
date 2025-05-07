from django.urls import path
from .views import AltaView

urlpatterns = [
    path('signup/', AltaView.as_view(), name='signup'),
]