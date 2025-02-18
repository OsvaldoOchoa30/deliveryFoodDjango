from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('order/list', OrdersListViewPage.as_view(), name='order_list'),
    path('order/create/', OrderCrearViewPage.as_view(), name='order_create'),
    path('order/edit/<int:pk>/', OrderEditarViewPage.as_view(), name='order_edit'),
    path('order/delete/<int:pk>', OrderEliminarViewPage.as_view(), name='order_delete'),
    path('custumer/list', CustumerListViewPage.as_view(), name='custumer_list'),
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
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
