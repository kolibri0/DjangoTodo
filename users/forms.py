from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter name'}))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Name"
        self.fields['password'].label = "Pswd"


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Repeat Password'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter name'}))

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""
        self.fields['username'].label = "Name"
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Pswd"
        self.fields['password2'].label = "Pswd"
