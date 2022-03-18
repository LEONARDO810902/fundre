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
            'genero',
            'ocupation'
        )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'input-group-field'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo Electronico', 'class': 'input-group-field'}),
            'Nombres': forms.TextInput(attrs={'placeholder': 'Nombres', 'class': 'input-group-field'}),
            'Apellidos': forms.TextInput(attrs={'placeholder': 'Apellidos', 'class': 'input-group-field'}),
            'Genero': forms.Select(attrs={'placeholder': 'Genero', 'class': 'input-group-field'}),
            'ocupation': forms.Select(attrs={'placeholder': 'Ocupación', 'class': 'input-group-field'}),

        }

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


class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User
        fields = (
            'email',
            'nombres',
            'apellidos',
            'genero',
            'ocupation',
            'is_active',
        )
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Correo Electronico', 'class': 'input-group-field'}),
            'Nombres': forms.TextInput(attrs={'placeholder': 'Nombres', 'class': 'input-group-field'}),
            'Apellidos': forms.TextInput(attrs={'placeholder': 'Apellidos', 'class': 'input-group-field'}),
            'Genero': forms.Select(attrs={'placeholder': 'Genero', 'class': 'input-group-field'}),
            'ocupation': forms.Select(attrs={'placeholder': 'Ocupación', 'class': 'input-group-field'}),
            'is_active': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'input-group-field'})

        }
