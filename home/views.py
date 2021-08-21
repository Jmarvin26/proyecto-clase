from home.models import Producto
from django.shortcuts import render
from .models import *

def vista_lista_producto(request):
    lista = Producto.objects.all()
    context = {'lista':lista}
    return render(request, 'lista_producto.html', context())

