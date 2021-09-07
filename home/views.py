from django.contrib.auth import authenticate
from home.models import Producto
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from .models import *

"""def vista_lista_producto(request):
    lista = Producto.objects.all()
    context = {'lista':lista}
    return render(request, 'lista_producto.html', context())
"""
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta Creada ' + user)

            return redirect(to='/login/')
    context = {'form':form}
    return render(request, 'register.html', context)



def login(request):
    context ={}
    return render(request, 'login_page.html', context)   