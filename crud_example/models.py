from django.db import models


class Cargo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return  format(self.nombre)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return format(self.nombre)


class Empleado(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    apellido= models.CharField(max_length=100,unique=True)
    fecha_naciento = models.DateField('YYYY-MM-DD')
    direccion = models.CharField(max_length=100,unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15,unique=True)
    Cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.CASCADE)
    Departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "empleado"




