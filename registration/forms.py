from django import forms
from .models import FactionUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = FactionUser
        fields = ('username', 'email', 'password', 'faction')
