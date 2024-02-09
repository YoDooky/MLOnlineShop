from django import forms
from django.contrib.auth import get_user_model


class ProfileUserForm(forms.ModelForm):
    name = forms.CharField(label='Name*', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    surname = forms.CharField(label='Surname*', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email*', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['name', 'surname', 'username', 'email']


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(
        label="Name*",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    surname = forms.CharField(
        label="Surname*",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email*",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label="Username*",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = get_user_model()
        fields = ['name', 'surname', 'username', 'email', 'password']
