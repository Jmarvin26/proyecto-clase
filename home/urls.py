
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.vista_lista_producto, name='vista_lista_producto'),
    path('registrar_usuario/', views.register, name='register'),
    path('login/', views.login, name='login'),
    #path('', views.loginPage, name="login"),
]

