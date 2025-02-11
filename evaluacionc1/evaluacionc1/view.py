from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Category, Customer, Delivery, OrderProduct, Orders, Product
from .vistas.formCategory import CategoryForm, CustomerForm, DeliveryForm, OrderProductForm, OrdersForm, ProductForm
from .vistas.views_base import BaseCreateView, BaseListView, BaseEditView, BaseDeleteView
from ..forms import OrdenForm, AsignarRepartidorForm

# Decorador para requerir autenticación en todas las vistas
def login_required_class_based_view(cls):
    return method_decorator(login_required, name='dispatch')(cls)

class HomePageView(TemplateView):
    template_name = 'home.html'  # Usará home.html que extiende de base.html
    
    @method_decorator(login_required)  # Asegura que solo usuarios logueados puedan ver la página
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

