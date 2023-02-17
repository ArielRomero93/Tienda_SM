from django.urls import path, include
from . import views
from.views import profile


urlpatterns = [

    #ruta, vista, clave, nombre
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),


    #CLIENTES
    path('clientes', views.clientes, name='clientes'),
    path('clientes/crear', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar', views.editar_cliente, name='editar_cliente'),
    path('clienteeliminar/<int:id>', views.eliminar_cliente, name='eliminar_cliente'),
    path('clientes/editar/<int:id>', views.editar_cliente, name='editar_cliente'),

    #CATEGORIA
    path('categorias', views.categorias, name='categorias'),
    path('categorias/crear', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar', views.editar_categoria, name='editar_categoria'),
    path('categoriaeliminar/<int:id>', views.eliminar_categoria, name='eliminar_categoria'),
    path('categorias/editar/<int:id>', views.editar_categoria, name='editar_categoria'),

    #PRODUCTO
    path('productos', views.productos, name='productos'),
    path('productos/crear', views.crear_producto, name='crear_producto'),
    path('productos/editar', views.editar_producto, name='editar_producto'),
    path('productoeliminar/<int:id>', views.eliminar_producto, name='eliminar_producto'),
    path('productos/editar/<int:id>', views.editar_producto, name='editar_producto'),

    # FACTURAS_VENTAS
    path('facturas_ventas', views.facturas_ventas, name='facturas_ventas'),
    path('facturas_ventas/crear', views.crear_factura_venta, name='crear_factura_venta'),
    path('facturas_ventas/editar', views.editar_factura_venta, name='editar_factura_venta'),
    path('factura_ventaeliminar/<int:id>', views.eliminar_factura_venta, name='eliminar_factura_venta'),
    path('facturas_ventas/editar/<int:id>', views.editar_factura_venta, name='editar_factura_venta'),

    # FACTURAS_VENTAS_LINEAS
    path('facturas_ventas_lineas', views.facturas_ventas_lineas, name='facturas_ventas_lineas'),
    path('facturas_ventas_lineas/crear', views.crear_factura_venta_linea, name='crear_factura_venta_linea'),
    path('facturas_ventas_lineas/editar', views.editar_factura_venta_linea, name='editar_venta_linea'),
    path('factura_venta_lineaeliminar/<int:id>', views.eliminar_factura_venta_linea, name='eliminar_factura_venta_linea'),
    path('facturas_ventas_lineas/editar/<int:id>', views.editar_factura_venta_linea, name='editar_factura_venta_linea'),

    #PROVEEDORES
    path('proveedores', views.proveedores, name='proveedores'),
    path('proveedores/crear', views.crear_proveedores, name='crear_proveedores'),
    path('proveedores/editar', views.editar_proveedores, name='editar_proveedores'),
    path('proveedoresliminar/<int:id>', views.eliminar_proveedores, name='eliminar_proveedores'),
    path('proveedores/editar/<int:id>', views.editar_proveedores, name='editar_proveedores'),

    #PEDIDOS
    path('pedidos', views.pedidos, name='pedidos'),
    path('pedidos/crear', views.crear_pedidos, name='crear_pedidos'),
    path('pedidos/editar', views.editar_pedidos, name='editar_pedidos'),
    path('pedidoseliminar/<int:id>', views.eliminar_pedidos, name='eliminar_pedidos'),
    path('pedidos/editar/<int:id>', views.editar_pedidos, name='editar_pedidos'),

    #Impresiones

]