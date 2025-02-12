from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from .models import Category, Customer, Delivery, OrderProduct, Orders, Product
from .vistas.formCustomer import FormCustomer
from .vistas.formCategory import FormCategory
from .vistas.formDelivery import FormDelivery
from .vistas.formOrders import FormOrders
from .vistas.formProduct import FormProduct


def login_required_class_based_view(cls):
    return method_decorator(login_required, name='dispatch')(cls)


class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')


class OrderViewPage(View):
    def get(self, request):
        form = FormOrders()
        return render(request, 'create_order.html', {'form': form})

    def post(self, request):
        form = FormOrders(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'create_order.html', {'form': form})


class OrderEditarViewPage(View):
    def get(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        form = FormOrders(instance=order)
        return render(request, 'create_order.html', {'form': form})

    def put(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        form = FormOrders(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Orden actualizada correctamente'})
        return JsonResponse({'error': form.errors}, status=400)


class OrderEliminarViewPage(View):
    def delete(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        order.delete()
        return JsonResponse({'message': 'Orden eliminada correctamente'})


class CustumerCrearViewPage(View):
    def get(self, request):
        form = FormCustomer()
        return render(request, 'create_custumer.html', {'form': form})

    def post(self, request):
        form = FormCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'create_custumer.html', {'form': form})


class CustumerEditarViewPage(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = FormCustomer(instance=customer)
        return render(request, 'update_custumer.html', {'form': form})

    def put(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = FormCustomer(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Cliente actualizado correctamente'})
        return JsonResponse({'error': form.errors}, status=400)


class CustumerEliminarViewPage(View):
    def delete(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return JsonResponse({'message': 'Cliente eliminado correctamente'})
