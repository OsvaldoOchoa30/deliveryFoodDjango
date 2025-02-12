from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Category, Customer, Delivery, OrderProduct, Orders, Product

from .vistas.formCustomer import FormCustomer
from .vistas.formCategory import FormCategory
from .vistas.formDelivery import FormDelivery
from .vistas.formOrders import FormOrders
from .vistas.formProduct import FormProduct


def login_required_class_based_view(cls):
    return method_decorator(login_required, name='dispatch')(cls)


class HomePageView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class OrdersListViewPage(TemplateView):
    template_name = "list_orders.html"
    model = Orders
    
    def get_context_data(self, **kwarqs):
        context = super().get_context_data(**kwarqs)
        context["lista"] = self.model.objects.all()
        return context

class OrderViewPage(TemplateView):
    template_name = 'create_order.html'

    def get(self, request, *args, **kwargs):
        form = FormOrders()
        return self.render_to_response({'form': form})
    
    def post(self, request, *args, **kwargs):
        form = FormOrders(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({'form': form})

class OrderEditarViewPage(TemplateView): 
    template_name = 'create_order.html'
    def get(self, request, pk,*args, **kwargs):
        order = get_object_or_404(Orders, pk=pk)
        form =  FormOrders(request.POST); 
        return self.render_to_response({'form': form})
 
    def post(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Orders, pk=pk)
        form = FormOrders(request.POST, instance=Orders)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({'form': form})

class OrderEliminarViewPage(TemplateView):
    template_name = 'delete_order.html'

    def get(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Orders, pk=pk)
        return self.render_to_response({'order': custumer})

    def post(self, request, pk, *args, **kwargs):
        custumer = get_object_or_404(Customer, pk=pk)
        custumer.delete()
        return redirect('home')  

class CustumerCrearViewPage(TemplateView):
    template_name = 'create_custumer.html'

    def get(self, request, *args, **kwargs):
        form = FormCustomer()
        return self.render_to_response({'form': form})
    
    def post(self, request, *args, **kwargs):
        form = FormCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({'form': form})

class CustumerEditarViewPage(TemplateView): 
    template_name = 'update_custumer.html'
    def get(self, request, pk,*args, **kwargs):
        custumer = get_object_or_404(Customer, pk=pk)
        form =  FormCustomer(request.POST); 
        return self.render_to_response({'form': form});
 
    def post(self, request, pk, *args, **kwargs):
        custumer = get_object_or_404(Customer, pk=pk)
        form = FormCustomer(request.POST, instance=custumer)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({'form': form})        

class CustumerEliminarViewPage(TemplateView):
    template_name = 'delete_custumer.html'

    def get(self, request, pk, *args, **kwargs):
        custumer = get_object_or_404(Customer, pk=pk)
        return self.render_to_response({'order': custumer})

    def post(self, request, pk, *args, **kwargs):
        custumer = get_object_or_404(Customer, pk=pk)
        custumer.delete()
        return redirect('home')