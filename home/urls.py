
from django.urls import path
from . import views
urlpatterns = [
    path('', views.vista_lista_producto, name='vista_lista_producto'),
]

