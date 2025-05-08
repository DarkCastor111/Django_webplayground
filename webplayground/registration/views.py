# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormCustom, PerfilUpdateFormCustom, PerfilEmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class AltaView(CreateView):
    form_class = UserCreationFormCustom
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    # Pagina de redireccion (para añadir ?register en el url)
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    # Modificar el formulario
    def get_form(self, form_class=None):
        # Recuperar el formulario
        form = super(AltaView, self).get_form()
        # Modificar
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Su correo electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        form.fields['username'].label = ''
        form.fields['email'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''

        return form

@method_decorator(login_required, name='dispatch')
class PerfilUpdateView(UpdateView):

    form_class = PerfilUpdateFormCustom
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # Recuperar el objeto que se va editar : Profile
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
@method_decorator(login_required, name='dispatch')
class PerfilEmailView(UpdateView):

    form_class = PerfilEmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # Recuperar el objeto que se va editar : User
        user = self.request.user
        return user
    
    # Modificar el formulario
    def get_form(self, form_class=None):
        # Recuperar el formulario
        form = super(PerfilEmailView, self).get_form()
        # Modificar
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Su correo electrónico'})
        form.fields['email'].label = ''
        return form