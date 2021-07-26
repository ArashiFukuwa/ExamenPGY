from django.contrib.auth import authenticate,login as django_login
from django.contrib.auth.forms import AuthenticationForm
from django.core import paginator
from app.forms import ProductoForm,UsuarioCreationForm, suscriptorForm
from app.models import Producto
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.

def index (request):
    return render(request,'app/index.html')


def productos (request):
    productosAll = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator=Paginator(productosAll, 6)
        productosAll= paginator.page(page)
    except:
        raise Http404
    
    datos = {
        'listasProductos' : productosAll,
        'paginator' : paginator
    }
    return render(request,'app/productos.html',datos)

def contacto (request):
    return render(request,'app/contacto.html')
@permission_required('app.add_producto')
def agregar_producto (request):
    datos = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente"
        
        datos ['form'] = formulario

    return render(request,'app/agregar_productos.html',datos) 
@permission_required('app.change_producto')
def modificar_producto (request,id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente"
            datos['form'] = formulario

    return render(request,'app/agregar_productos.html',datos) 
@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="productos")


def quiensomos(request):
    return render(request,'app/quiensomos.html')


def login (request):
    return render(request,'app/login.html')

def horario(request):
    return render(request,'app/horario.html')


def registro_usuario(request):
    datos = {
        'form' : UsuarioCreationForm()
    }

    if request.method == 'POST':
        formulario = UsuarioCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            django_login(request, user)
            return redirect(to="index")
        datos['form'] = formulario

    return render(request, 'registration/signup.html', datos)




def suscriptor (request):
    data ={ 
        'form' : suscriptorForm()
    }

    if request.method == 'POST':
        formulario = suscriptorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario

    return render(request,'app/suscriptor.html',data)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer