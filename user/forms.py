from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    '''
        Formulaire de connexion
    '''
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': 'adresse email',
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
        }
    ))


class RegisterForm(UserCreationForm):
    '''
        Formulaire d'inscription
    '''
    
    
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom d\' utilisateur',
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email',
        }
    ))

    
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Mot de passe',
            'class': 'width-2',
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Confirmer le mot de passe',
            'class': 'width-2',
        }
    ))

    
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = (
            'username',
            'email',
            'password1', 
            'password2',
        )    