from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Proveedores(models.Model):
    numeroDocumento = models.CharField(primary_key=True, max_length=13, help_text='CUIT, CUIL ó DNI', blank=True)
    nombre = models.CharField(max_length=40, help_text='Nombre del proveedor')
    direccion = models.CharField(max_length=40, blank=True)
    localidad = models.CharField(max_length=30, blank=True)
    provincia = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=50, help_text='Email', blank=True, null= False)
    telefono = models.CharField(max_length=20, unique= True, null= False)

    def __str__(self):
        return self.nombre


class PagoProveedores(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(help_text='Fecha de pago', verbose_name='Fecha pago')
    proveedor = models.ForeignKey(Proveedores,on_delete=models.CASCADE, help_text='Proveedor', blank=True)


class Categoria(models.Model):
    categoria = models.CharField(max_length= 40, help_text='Categoria de Prenda')

    def __str__(self):
        return self.categoria

class Productos(models.Model):
    nombre = models.CharField(max_length=50, help_text='Producto')
    talleN = models.IntegerField(help_text='Talle en numero', null=True)
    stock = models.IntegerField(verbose_name='Stock')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name='Precio')

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    fecha = models.DateField(help_text='Fecha de carga del pedido')
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, help_text='Proveedor')
    idProducto = models.ForeignKey(Productos, on_delete=models.CASCADE,help_text='Productos')
    factura = models.IntegerField(blank=True, null=True, verbose_name='NumeroFactura')
    remito = models.IntegerField(blank=True, null=True, verbose_name='NumeroRemito')

    def __str__(self):
        return str(self.fecha) + str(self.proveedor)


class ProductosPedidos(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(help_text='Fecha de carga del pedido', blank=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, help_text='Pedido')
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, help_text='Proveedor')
    producto = models. ForeignKey(Productos, on_delete=models.CASCADE, help_text='Producto')

    def __str__(self):
        return  str(self.fecha) + str(self.pedido) + str(self.proveedor)

#Ventas

class Clientes(models.Model):
    numeroDocumento = models.CharField(primary_key=True, max_length=13, help_text='CUIT, CUIL ó DNI', blank=True)
    nombre = models.CharField(max_length=20, help_text='Nombre', verbose_name='Nombre')
    direccion = models.CharField(max_length=40, help_text='Calle y numero', verbose_name='Direccion', blank=True,default="")
    localidad = models.CharField(max_length=20, verbose_name='Localidad', default="", blank=True)
    provincia = models.CharField(max_length=20, verbose_name='Provincia', default="", blank=True)
    email = models.EmailField(max_length=50, help_text='Email', blank=True, )
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Telefono', null= True)

    def __str__(self):
        return self.nombre


class FacturasVentas(models.Model):
    fecha = models.DateField(help_text='Fecha de emisión')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cliente) + " / " + str(self.fecha)

class FacturaVentaLinea(models.Model):
    factura = models.ForeignKey(FacturasVentas, on_delete=models.CASCADE, help_text='Id de factura')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    importe = models.IntegerField(verbose_name='Importe')
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.producto) + " / " + str(self.cantidad) + " Un."

class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(help_text='fecha de emision', verbose_name='Fecha')
    factura = models.ForeignKey(FacturasVentas, on_delete=models.CASCADE, help_text='Factura')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, help_text='Cliente')

    def __str__(self):
        return str(self.id) + str(self.cliente)