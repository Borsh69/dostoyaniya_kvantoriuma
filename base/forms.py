from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['login', 'password']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input', type: 'password'})
        }


