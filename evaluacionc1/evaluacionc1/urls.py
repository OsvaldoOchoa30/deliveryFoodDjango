from django.contrib import admin
from django.urls import path
from .view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('custumer/create', CustumerCrearViewPage.as_view(),name='custumer_create'), 
    path('custumer/edit/<int:pk>/', CustumerEditarViewPage.as_view(), name='custumer_edit'),
    path('custumer/delete/<int:pk>', CustumerEliminarViewPage.as_view(), name='custumer_delete'),
    path('category/list', CategoryListViewPage.as_view(), name='category_list'),
    path('category/create', CategoryCrearViewPage.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryEditarViewPage.as_view(), name='category_edit'),
    path('category/delete/<int:pk>', CategoryEliminarViewPage.as_view(), name='category_delete'),
    path('delivery/list', DeliveryListViewPage.as_view(), name='delivery_list'),
    path('delivery/create', DeliveryCrearViewPage.as_view(), name='delivery_create'),
    path('delivery/edit/<int:pk>/', DeliveryEditarViewPage.as_view(), name='delivery_edit'),
    path('delivery/delete/<int:pk>', DeliveryEliminarViewPage.as_view(), name='delivery_delete'),
    path('product/list', ProductListViewPage.as_view(), name='product_list'),
    path('product/create', ProductCrearViewPage.as_view(), name='product_create'),
    path('product/edit/<int:pk>/', ProductEditarViewPage.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', ProductEliminarViewPage.as_view(), name='product_delete'),
]
