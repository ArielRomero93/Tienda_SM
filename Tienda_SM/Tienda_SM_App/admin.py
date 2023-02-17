from django.contrib import admin

from Tienda_SM_App.models import Proveedores, Clientes, Productos, Pedidos, Ventas, PagoProveedores, \
    ProductosPedidos, Categoria, FacturaVentaLinea, FacturasVentas


# Register your models here.

class adminSM(admin.ModelAdmin):
    list_display = ('nombre','fecha')

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('categoria'),
    ordering = ['categoria']

class ProductoAdmin(admin.ModelAdmin):
    ordering = ['nombre'],
    autocomplete_fields = ['categoria']


admin.site.site_header = 'Tienda SM'
admin.site.site_title = 'Tienda SM'
admin.site.index_title = 'Archivos'

admin.site.register(Proveedores)
admin.site.register(Productos)
admin.site.register(Pedidos)
admin.site.register(Ventas)
admin.site.register(PagoProveedores)
admin.site.register(ProductosPedidos)
admin.site.register(Clientes)
admin.site.register(Categoria)
admin.site.register(FacturaVentaLinea)
admin.site.register(FacturasVentas)
