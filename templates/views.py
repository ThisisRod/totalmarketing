from django import forms
from .models import Paquete, Comentario, Compra

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['nombre', 'descripcion', 'precio']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['paquete', 'cantidad']
        widgets = {
            'paquete': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar')
