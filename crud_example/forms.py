from django import forms
from .models import Empleado,Cargo,Departamento


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields=[
        'nombre',
        'apellido',
        'fecha_naciento',
        'direccion',
        'correo',
        'telefono',
        'Cargo',
        'Departamento',
        ]
        labels={
         'nombre':'Nombre Empleado',
         'apellido':'Apellido Empleado',
         'fecha_naciento':'Fecha Nacimiento',
         'direccion':'Dirección:',
         'correo':'Correo:',
         'telefono':'Telefono',
         'Cargo':'Cargo del Empleado:',
         'Departamento':'Departamento:',

        }
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_naciento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'Cargo': forms.Select(attrs={'class': 'form-control'}),
            'Departamento': forms.Select(attrs={'class': 'form-control'}),

        }

class CargoForm(forms.ModelForm):
    class Meta:
        model=Cargo
        fields=[
            'nombre',
            'descripcion',

        ]
        labels={
            'nombre':'Nombre del Cargo',
            'descripcion':'Breve resumen del cargo',

        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }

class DepartForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields=[
            'nombre',

        ]
        labels={
            'nombre':'Nombre del Cargo',

        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),

        }