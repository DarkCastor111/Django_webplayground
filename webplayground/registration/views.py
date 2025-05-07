# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class AltaView(CreateView):
    form_class = UserCreationFormWithEmail
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
