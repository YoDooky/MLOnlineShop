from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }))


class ProfileUserForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    first_name = forms.CharField(label='Name*', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Surname*', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email*', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['image', 'first_name', 'last_name', 'username', 'email']


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label="Name*",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        })
    )
    last_name = forms.CharField(
        label="Surname*",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your surname'
        })
    )
    email = forms.EmailField(
        label="Email*",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    username = forms.CharField(
        label="Username*",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat your password'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exist')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exist')
        return username


# class UserPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(
#         label="Old password",
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={"autocomplete": "current-password", "autofocus": True}
#         ),
#     )
#     new_password1 = forms.CharField(
#         label="New password",
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#         strip=False,
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     new_password2 = forms.CharField(
#         label="New password confirmation",
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#     )
