from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your email'}
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter your password'}
        )
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
        return self.cleaned_data


class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter your full name'}
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your email'}
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter a strong password'}
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Confirm your password'}
        )
    )

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']


class ManagerLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password',
                  'is_manager', 'is_active', 'is_admin',]

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Enter your full name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter a strong password'
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['style'] = 'background-color: #e9ecef;'
        self.fields['full_name'].label = 'Full Name'
        self.fields['email'].label = 'Email (You cannot change your email)'
        self.fields['password'].label = 'Password (You cannot change your password)'
