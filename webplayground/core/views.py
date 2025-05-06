from django.views.generic.base import TemplateView
from django.shortcuts import render

class InicioPageView(TemplateView):
    template_name = "core/home.html"

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Mi super Web Playground"
        return context
    '''
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"titulo_pagina":"Mi giga Web Playground"})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"