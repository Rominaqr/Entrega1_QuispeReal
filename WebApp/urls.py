from django.urls import path
from WebApp import views

urlpatterns = [
    path('index/', views.index, name="home"),
    path('registrar/', views.altaUsuario, name="registrar"),
    path('datosUsuario/<idUsuario>', views.altaDatosUsuario, name="datosUsuario"),
    path('musicos/', views.inicioMusicos, name="inicioMusicos"),
    path('musicosIngresar/', views.altaMusicos, name="musicosIngresar"),
    path('buscarMusico/', views.buscarMusico, name="buscarMusico"),
    path('contacto/', views.altaContacto, name="contacto"),
]
