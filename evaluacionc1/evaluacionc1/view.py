from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .vistas.formCustomer import FormCustomer
from .models import Category, Customer, Delivery, OrderProduct, Orders, Product


def login_required_class_based_view(cls):
    return method_decorator(login_required, name='dispatch')(cls)


class HomePageView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class OrdersCreateViewPage(TemplateView):
    template_name = 'order_form.html'
    
    def get(self, request, *args, **kwargs):
        form = OrderForm()
        return self.render_to_response({'form': form})
    
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({'form': form})
    
class OrdersEditarPageView(TemplateView):
    template_name = 'order_form.html'

    def get(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Orders, pk=pk)
        form = OrderForm(instance=order)
        return self.render_to_response({'form': form})
    
    def post(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Orders, pk=pk)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({'form': form})
    
class OrdersEliminarPageView(TemplateView):
    template_name = 'order_confirm_delete.html'

    def get(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Orders, pk=pk)
        return self.render_to_response({'order': order})

    def post(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Orders, pk=pk)
        order.delete()
        return redirect('home')
    

class CustumerViewPage(TemplateView):
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
