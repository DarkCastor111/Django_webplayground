from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, y debe ser válido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email_form = self.cleaned_data.get('email')
        if User.objects.filter(email=email_form).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email_form