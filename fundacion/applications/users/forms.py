from pyexpat import model
from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserCreateForm(forms.ModelForm):

    password1 = forms.CharField(
        label=("Contraseña"),
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Contraseña'
                   }
        )
    )

    password2 = forms.CharField(
        label=("Contraseña"),
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Repetir Contraseña'
                   }
        )
    )

    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero'
        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error(
                'password2', 'Las contraseñas no son identicas verificar')


class LoginForm(forms.Form):
    username = forms.CharField(
        label="username",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'style': '{ margin: 10px }',
            }
        )
    )
    password = forms.CharField(
        label="password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuarios no correctos')

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label=("Contraseña"),
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Contraseña Actual '
                   }
        )
    )

    password2 = forms.CharField(
        label=("Contraseña"),
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Contraseña Nueva '
                   }
        )
    )
