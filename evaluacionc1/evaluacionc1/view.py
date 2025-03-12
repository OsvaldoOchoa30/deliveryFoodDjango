from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render

from .models import Category, Customer, Delivery, OrderProduct, Orders, Product

from .vistas.formCustomer import FormCustomer
from .vistas.formCategory import FormCategory
from .vistas.formDelivery import FormDelivery
from .vistas.formOrders import FormOrders
from .vistas.formProduct import FormProduct

def login_required_class_based_view(cls):
    return method_decorator(login_required, name='dispatch')(cls)

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/login/'

class BaseListView(LoginRequiredMixin, TemplateView):
    model = None
    template_name = ""
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista"] = self.model.objects.all()
        return context

class BaseCreateView(LoginRequiredMixin, TemplateView):
    template_name = ''
    form_class = None
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self.render_to_response({'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({'form': form})

class BaseUpdateView(LoginRequiredMixin, TemplateView):
    template_name = ''
    model = None
    form_class = None
    login_url = '/login/'

    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=instance)
        return self.render_to_response({'form': form})

    def post(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=pk)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({'form': form})

class BaseDeleteView(LoginRequiredMixin, TemplateView):
    template_name = ''
    model = None
    login_url = '/login/'

    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=pk)
        return self.render_to_response({'object': instance})

    def post(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=pk)
        instance.delete()
        return redirect('home')

class OrdersListViewPage(BaseListView):
    template_name = "list_orders.html"
    model = Orders

class OrderCrearViewPage(BaseCreateView):
    template_name = 'create_order.html'
    form_class = FormOrders

class OrderEditarViewPage(BaseUpdateView):
    template_name = 'update_order.html'
    model = Orders
    form_class = FormOrders

class OrderEliminarViewPage(BaseDeleteView):
    template_name = 'delete_order.html'
    model = Orders

class CustumerListViewPage(BaseListView):
    template_name = "list_custumers.html"
    model = Customer

class CustumerCrearViewPage(BaseCreateView):
    template_name = 'create_custumer.html'
    form_class = FormCustomer

class CustumerEditarViewPage(BaseUpdateView):
    template_name = 'update_custumer.html'
    model = Customer
    form_class = FormCustomer

class CustumerEliminarViewPage(BaseDeleteView):
    template_name = 'delete_custumer.html'
    model = Customer

class CategoryListViewPage(BaseListView):
    template_name = "list_categories.html"
    model = Category

class CategoryCrearViewPage(BaseCreateView):
    template_name = 'create_category.html'
    form_class = FormCategory

class CategoryEditarViewPage(BaseUpdateView):
    template_name = 'update_category.html'
    model = Category
    form_class = FormCategory

class CategoryEliminarViewPage(BaseDeleteView):
    template_name = 'delete_category.html'
    model = Category

class DeliveryListViewPage(BaseListView):
    template_name = "list_deliveries.html"
    model = Delivery

class DeliveryCrearViewPage(BaseCreateView):
    template_name = 'create_delivery.html'
    form_class = FormDelivery

class DeliveryEditarViewPage(BaseUpdateView):
    template_name = 'update_delivery.html'
    model = Delivery
    form_class = FormDelivery

class DeliveryEliminarViewPage(BaseDeleteView):
    template_name = 'delete_delivery.html'
    model = Delivery

class ProductListViewPage(BaseListView):
    template_name = "list_products.html"
    model = Product

class ProductCrearViewPage(BaseCreateView):
    template_name = 'create_product.html'
    form_class = FormProduct

class ProductEditarViewPage(BaseUpdateView):
    template_name = 'update_product.html'
    model = Product
    form_class = FormProduct

class ProductEliminarViewPage(BaseDeleteView):
    template_name = 'delete_product.html'
    model = Product

class EnviarAutor(TemplateView):
    template_name = 'createEntitie.html'
