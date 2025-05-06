from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffNecesarioMixin(object):
    pass
    """
    Control de que el usuario sea del staff

    Con mixin :
    """
#    def dispatch(self, request, *args, **kwargs):
#        if not request.user.is_staff:
#            return redirect(reverse_lazy('admin:login'))
#
#        return super(StaffNecesarioMixin, self).dispatch(request, *args, **kwargs)

    """
    Efecto de el decorador :
    """
#    @method_decorator(staff_member_required)
#    def dispatch(self, request, *args, **kwargs):
#        return super(StaffNecesarioMixin, self).dispatch(request, *args, **kwargs)
    
# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(StaffNecesarioMixin, CreateView):
    # StaffNecesarioMixin : no utilisado si utilizamos el decorador
    model = Page
    form_class = PageForm

    # Pagina de redireccion
    success_url = reverse_lazy('pages:pages')

    '''
    def get_success_url(self):
        return reverse('pages:pages')
    '''


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(StaffNecesarioMixin, UpdateView):
    # StaffNecesarioMixin : no utilisado si utilizamos el decorador
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    # Pagina de redireccion
    def get_success_url(self):
        return reverse('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')    
class PageDelete(StaffNecesarioMixin, DeleteView):
    # StaffNecesarioMixin : no utilisado si utilizamos el decorador
    model = Page
    success_url = reverse_lazy('pages:pages')

