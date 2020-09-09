from django.shortcuts import render, redirect
from .forms import EmpleadoForm,CargoForm,DepartForm
from .models import Empleado ,Departamento, Cargo


#Vistas del CRUD EMPLEADO
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


## FUNCIONES DEL CRUD TABLA CARGO
#FUNCION CREAR
def cargo_crear(request):
    if request.method == "POST":
        form = CargoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('cargo')
            except:
                pass
    else:
        form = CargoForm()
    return render(request, 'registro_cargo.html', {'form': form})

#FUNCION LISTAR
def listar_cargo(request):
    cargo = Cargo.objects.all()
    return render(request, "lista_cargo.html", {'Cargo':cargo})

#FUNCION ELIMINAR
def eliminar_cargo(request, id):
    cargo = Cargo.objects.get(id=id)
    cargo.delete()
    return redirect('cargo')

#FUNCION EDITAR
def editar_cargo(request, id):
    cargo = Cargo.objects.get(id=id)
    if request.method == 'GET':
        form = CargoForm(instance=cargo)
    else:
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargo')
    return render(request,'editar_cargo.html',{'form':form})

#CRUD TABLA DEPARTAMENTO

#FUNCION CREAR
def crear_departamento(request):
    if request.method == "POST":
        form = DepartForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_depart')
            except:
                pass
    else:
        form = CargoForm()
    return render(request, 'registro_depart.html', {'form': form})

#FUNCION LISTAR
def listar_depart(request):
    departamento = Departamento.objects.all()
    return render(request, "lista_depart.html", {'Departamento':departamento})

#FUNCION ELIMINAR
def eliminar_depart(request, id):
    departamento = Departamento.objects.get(id=id)
    departamento.delete()
    return redirect('listar_depart')

#FUNCION EDITAR
def editar_depart(request, id):
    departamento = Departamento.objects.get(id=id)
    if request.method == 'GET':
        form = DepartForm(instance=departamento)
    else:
        form = DepartForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('listar_depart')
    return render(request,'editar_depart.html',{'form':form})
