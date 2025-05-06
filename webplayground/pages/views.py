from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffNecesarioMixin(object):
    """
    Control de que el usuario sea del staff
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))

        return super(StaffNecesarioMixin, self).dispatch(request, *args, **kwargs)
    
# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(StaffNecesarioMixin, CreateView):
    model = Page
    form_class = PageForm

    # Pagina de redireccion
    success_url = reverse_lazy('pages:pages')

    '''
    def get_success_url(self):
        return reverse('pages:pages')
    '''



class PageUpdate(StaffNecesarioMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    # Pagina de redireccion
    def get_success_url(self):
        return reverse('pages:update', args=[self.object.id]) + '?ok'
    
class PageDelete(StaffNecesarioMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

