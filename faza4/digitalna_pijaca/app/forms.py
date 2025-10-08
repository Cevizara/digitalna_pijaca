from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Korisnik

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Korisnik
        fields = ('email', 'ime', 'sifra')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")  # koristi email umesto username-a
