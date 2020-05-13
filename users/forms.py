from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import Profile

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Password'})
        
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Re-enter Password'})

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Email'})
      


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Bio'})
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Last Name'})