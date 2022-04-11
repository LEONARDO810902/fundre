from django import forms

# modelos de esal

from .models import Esal


class EsalCreateForm(forms.ModelForm):
    class Meta:
        model = Esal
        fields = (
            'titulo',
            'resumen',
            'archivo',
            'vigencia',
            'publicar'

        )
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control', }),
            # 'archivo':  forms.FileField(),
            'vigencia': forms.Select(attrs={'class': 'form-control-lg'}),
            'publicar': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input'})
        }
