from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Clientes, Categoria, Productos, FacturasVentas, FacturaVentaLinea, Proveedores, Pedidos
from .forms import ClienteForm, CategoriaForm, ProductoForm, FacturasVentasForm,FacturasVentasLineasForm, ProveedoresForm,PedidosForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def profile(request):
    return render(request, 'paginas/profile.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.success(request, "Hubo un error, intente nuevamente" )
            return redirect('login')
    else:
        return render(request, 'registration/login2.html', {})


def logout_user(request):
     logout(request)
     messages.success(request,("Te deslogueaste...!"))
     return redirect('inicio')




#CLIENTES

def clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes/index.html', {'clientes': clientes})

def  crear_cliente(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crear.html', {'formulario': formulario})


def  editar_cliente(request, id):
    cliente = Clientes.objects.get(numeroDocumento=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/editar.html', {'formulario': formulario})

def  eliminar_cliente(request, id):
    cliente = Clientes.objects.get(numeroDocumento=id)
    cliente.delete()
    return redirect('clientes')

#CATEGORIA

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/index.html', {'categorias': categorias})

def  crear_categoria(request):
    formulario = CategoriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('categorias')
    return render(request, 'categorias/crear.html', {'formulario': formulario})


def  editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    formulario = CategoriaForm(request.POST or None, request.FILES or None, instance=categoria)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('categorias')
    return render(request, 'categorias/editar.html', {'formulario': formulario})

def  eliminar_categoria(request, id):
    categoria= Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categorias')


#PRODUCTOS

def productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})

def  crear_producto(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html', {'formulario': formulario})


def  editar_producto(request, id):
    producto = Productos.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/editar.html', {'formulario': formulario})

def  eliminar_producto(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('productos')


#FACTURAS_VENTAS

def facturas_ventas(request):
    facturas_ventas = FacturasVentas.objects.all()
    return render(request, 'facturas_ventas/index.html', {'facturas_ventas': facturas_ventas})

def  crear_factura_venta(request):
    formulario = FacturasVentasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('facturas_ventas')
    return render(request, 'facturas_ventas/crear.html', {'formulario': formulario})


def  editar_factura_venta(request, id):
    factura_venta = FacturasVentas.objects.get(id=id)
    formulario = FacturasVentasForm(request.POST or None, request.FILES or None, instance=factura_venta)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('facturas_ventas')
    return render(request, 'facturas_ventas/editar.html', {'formulario': formulario})

def  eliminar_factura_venta(request, id):
    factura_venta = FacturasVentas.objects.get(id=id)
    factura_venta.delete()
    return redirect('facturas_ventas')


#FACTURAS_VENTAS_LINEA

def facturas_ventas_lineas(request):
    facturas_ventas_lineas = FacturaVentaLinea.objects.all()
    return render(request, 'facturas_ventas_lineas/index.html', {'facturas_ventas_lineas': facturas_ventas_lineas})

def  crear_factura_venta_linea(request):
    formulario = FacturasVentasLineasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('facturas_ventas_lineas')
    return render(request, 'facturas_ventas_lineas/crear.html', {'formulario': formulario})


def  editar_factura_venta_linea(request, id):
    factura_venta_linea = FacturaVentaLinea.objects.get(id=id)
    formulario = FacturasVentasLineasForm(request.POST or None, request.FILES or None, instance=factura_venta_linea)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('facturas_ventas_lineas')
    return render(request, 'facturas_ventas_lineas/editar.html', {'formulario': formulario})

def  eliminar_factura_venta_linea(request, id):
    factura_venta_linea = FacturaVentaLinea.objects.get(id=id)
    factura_venta_linea.delete()
    return redirect('facturas_ventas_lineas')


#PROVEEDORES
def proveedores(request):
   proveedores = Proveedores.objects.all()
   return render(request, 'proveedores/index.html', {'proveedores': proveedores})


def  crear_proveedores(request):
   formulario = ProveedoresForm(request.POST or None, request.FILES or None)
   if formulario.is_valid():
       formulario.save()
       return redirect('proveedores')
   return render(request, 'proveedores/crear.html', {'formulario': formulario})

def  editar_proveedores(request, id):
   proveedores= Proveedores.objects.get(numeroDocumento=id)
   formulario = ProveedoresForm(request.POST or None, request.FILES or None, instance=proveedores)
   if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('proveedores')
   return render(request, 'proveedores/editar.html', {'formulario': formulario})

def eliminar_proveedores(request, id):
   proveedores = Clientes.objects.get(numeroDocumento=id)
   proveedores.delete()
   return redirect('proveedores')

#PEDIDOS
def pedidos(request):
   pedidos= Pedidos.objects.all()
   return render(request, 'pedidos/index.html', {'pedidos': pedidos})


def crear_pedidos(request):
   formulario = PedidosForm(request.POST or None, request.FILES or None)
   if formulario.is_valid():
       formulario.save()
       return redirect('pedidos')
   return render(request, 'pedidos/crear.html', {'formulario': formulario})

def editar_pedidos(request, id):
   pedidos= Pedidos.objects.get(id=id)
   formulario = PedidosForm(request.POST or None, request.FILES or None, instance=pedidos)
   if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('pedidos')
   return render(request, 'pedidos/editar.html', {'formulario': formulario})

def eliminar_pedidos(request, id):
   pedidos = Pedidos.objects.get(id=id)
   pedidos.delete()
   return redirect('pedidos')
