from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'autor',
            'anio_publicacion',
            'disponible',
        ]

        labels = {
            'titulo': 'Título del libro',
            'autor': 'Autor',
            'anio_publicacion': 'Año de publicación',
            'disponible': 'Disponible para préstamo',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el título',
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el autor',
            }),
            'anio_publicacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 2020',
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

from django import forms
from .models import Libro, Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'documento', 'correo']

        labels = {
            'nombre': 'Nombre completo',
            'documento': 'Número de documento',
            'correo': 'Correo electrónico',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo',
            }),
            'documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de documento',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
            }),
        }

    def clean_anio_publicacion(self):
        anio = self.cleaned_data.get('anio_publicacion')

        if anio is not None and anio > 2026:
            raise forms.ValidationError(
                'El año de publicación no puede ser futuro.'
            )

        return anio