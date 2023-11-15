from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account


class SignUpForm(UserCreationForm):
    steamId = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'steamId', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username','password']
