from django.conf.urls import url
from usuario import views


urlpatterns = [
    url(r'Registra',views.registro_usuario.as_view(),name='registro_usuario'),

]