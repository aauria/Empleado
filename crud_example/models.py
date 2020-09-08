from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    fecha_naciento = models.DateField('YYYY-MM-DD')
    direccion = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return '{} {}',format(self.nombre, self.apellido)


    class Meta:
        db_table = "empleado"

class Cargo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    Empleado = models.OneToOneField(Empleado, null=True, blank=True, on_delete=models.CASCADE)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    Empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}',format(self.nombre)
