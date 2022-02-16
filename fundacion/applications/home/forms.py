from django import forms

# modelos
from .models import Suscribirse, Contacto


class SuscribirseFoms(forms.ModelForm):
    class Meta:
        model = Suscribirse
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={'placeholder': 'Correo Electronico...',
                       'class': 'input-email'
                       }
            ),
        }


class ContactoFoms(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('__all__')
