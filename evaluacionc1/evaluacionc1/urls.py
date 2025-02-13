from django.contrib import admin
from django.urls import path
from .view import HomePageView, OrdersListViewPage, OrderViewPage, OrderEditarViewPage, OrderEliminarViewPage, CustumerCrearViewPage, CustumerEditarViewPage, CustumerEliminarViewPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('custumer/create', CustumerCrearViewPage.as_view(),name='custumer_create'), 
    path('custumer/edit/<int:pk>/', CustumerEditarViewPage.as_view(), name='custumer_edit'),
    path('custumer/delete/<int:pk>', CustumerEliminarViewPage.as_view(),name='custumer_delete'),
    path('order/list', OrdersListViewPage.as_view(), name='order_list')
]
