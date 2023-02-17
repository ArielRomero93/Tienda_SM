from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from Tienda_SM_App.models import FacturasVentas, FacturaVentaLinea
from Tienda_SM_App.forms import FacturasVentasForm

class FormsetFacturaVenta(FormView):
    template_name = ''