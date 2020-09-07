"""Empleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from crud_example import views
from django.contrib.auth.urls import views as login



urlpatterns = [
    path('', login.LoginView.as_view(template_name='login_2.html')),
    url('usuario', include('usuario.urls')),
    path('inicio',views.home,name='nuevo_inicio'),
    path('emp', views.emp,name="inicio"),
    path('show',views.listar_empleado,name='listar'),
    path('editar/<int:id>', views.editar_empleado,name='editar'),
    path('eliminar/<int:id>', views.eliminar,name='eliminar'),
    path('cargo',views.Cargo.as_view(),name='cargo'),
    path('crear_cargo/',views.crear_cargo.as_view(),name='crear_cargo'),
    path('admin/', admin.site.urls),

]