# user/forms.py

from django import forms
from django.core.exceptions import ValidationError

from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'px-4 py-2 w-full border border-gray-300 rounded-md focus:outline-none focus:border-blue-500',
        'placeholder': 'Your email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'px-4 py-2 w-full border border-gray-300 rounded-md focus:outline-none focus:border-blue-500',
        'placeholder': 'Your password'
    }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('This field is required.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('This field is required.')
        return password
    

class SignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'px-4 py-2 w-full border border-gray-300 rounded-md focus:outline-none focus:border-blue-500',
        'placeholder': 'Your name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'px-4 py-2 w-full border border-gray-300 rounded-md focus:outline-none focus:border-blue-500',
        'placeholder': 'Your email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'px-4 py-2 w-full border border-gray-300 rounded-md focus:outline-none focus:border-blue-500',
        'placeholder': 'Your password'
    }), min_length=6)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'px-4 py-2 w-full border border-gray-300 rounded-md focus:outline-none focus:border-blue-500',
        'placeholder': 'Confirm password'
    }))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('This field is required.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('This field is required.')
        if User.objects.filter(email=email).exists():
            raise ValidationError('User with this email already exists.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('This field is required.')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError('Passwords do not match.')
        return password2
    
    def save(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = User(name=name, email=email)
        user.set_password(password)
        user.save()
        return user
    
    