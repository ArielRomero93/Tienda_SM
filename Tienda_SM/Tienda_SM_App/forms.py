from django import forms
from .models import Clientes, Categoria, Productos,FacturasVentas, FacturaVentaLinea, Proveedores, Pedidos
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

#CLIENTES
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'


#CATEGORIAS

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


#PRODUCTO

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'})
        }
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['categoria'].widget.attrs.update({
        #         'class': 'form-select',
        #     })

#FACTURAS_VENTAS

class FacturasVentasForm(forms.ModelForm):
    class Meta:
        model = FacturasVentas
        fields = '__all__'

#FACTURAS_VENTAS_LINEAS

class FacturasVentasLineasForm(forms.ModelForm):
    class Meta:
        model = FacturaVentaLinea
        fields = '__all__'


#PROVEEDORES

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'

#PEDIDOS

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__'