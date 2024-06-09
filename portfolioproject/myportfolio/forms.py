from django import forms
from .models import Contacto

# Definición de un formulario basado en el modelo Contacto
class ContactoForm(forms.ModelForm):
    # Clase interna Meta que contiene la configuración del formulario
    class Meta:
        # Especifica el modelo del cual se creará el formulario
        model = Contacto
        # Define los campos del modelo que se incluirán en el formulario
        fields = ['nombre', 'email', 'mensaje']
        # Especifica los widgets personalizados para los campos del formulario
        widgets = {
            # Utiliza un widget de entrada de texto con una clase CSS 'form-control' para el campo 'nombre'
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            # Utiliza un widget de entrada de correo electrónico con una clase CSS 'form-control' para el campo 'email'
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # Utiliza un widget de área de texto con una clase CSS 'form-control' para el campo 'mensaje'
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }
