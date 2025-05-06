from django.urls import path
from .views import InicioPageView, SamplePageView

urlpatterns = [
    path('', InicioPageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
]