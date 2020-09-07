from django.shortcuts import render, redirect
from .forms import EmpleadoForm,CargoForm
from django.urls import reverse_lazy
from .models import Empleado , Departamento, Cargo
from django.views.generic import ListView,CreateView


# Create your views here.
def home(request, plantilla="inicio.html"):
    return render(request, plantilla);

def emp(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar')
            except:
                pass
    else:
        form = EmpleadoForm()
    return render(request, 'index.html', {'form': form})


def listar_empleado(request):
    empleado = Empleado.objects.all()
    return render(request, "show.html", {'Empleado':empleado})


def editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    if request.method == 'GET':
        form = EmpleadoForm(instance=empleado)
    else:
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar')
    return render(request,'edit.html',{'form':form})

def eliminar(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('listar')


#VISTAS CREADAS CON CLASES
class Cargo(ListView):
    model = Cargo
    template_name = 'lista_cargo.html'

class crear_cargo(CreateView):
    model = Cargo
    form = CargoForm
    template_name = 'registro_cargo.html'
    success_url = reverse_lazy('nuevo_inicio')