from django import forms
from .models import Empleado,Cargo


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

class CargoForm(forms.ModelForm):
    class Meta:
        model=Cargo
        fields=[
            'nombre',
            'descripcion',
            'Empleado',
        ]
        labels={
            'nombre':'Nombre del Cargo',
            'descripcion':'Breve resumen del cargo',
            'Empleado':'Nombre del empleado'
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'Empleado':forms.Select(attrs={'class': 'form-control'}),
        }