from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormCustom(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, y debe ser válido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email_form = self.cleaned_data.get('email')
        if User.objects.filter(email=email_form).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email_form
    
class PerfilUpdateFormCustom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio', 'link')
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3',}),
            'bio' : forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':"Su presentación"}),
            'link' : forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':"Enlace"}),
        }
        labels = {
            'avatar' : '',
            'bio' : '',
            'link' : '',

        }

class PerfilEmailForm(forms.ModelForm):

    email = forms.EmailField(required=True, help_text="Requerido, y debe ser válido")

    class Meta:
        model = User
        fields = ("email",)

    def clean_email(self):
        email_form = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email_form).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email_form
