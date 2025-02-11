from django.contrib import admin
from django.urls import path
from .view import HomePageView, OrdersCreateViewPage, OrdersEditarPageView, OrdersEliminarPageView, CustumerViewPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('order/create/', OrdersCreateViewPage.as_view(), name='order_create'),
    path('order/edit/<int:pk>/', OrdersEditarPageView.as_view(), name='order_edit'),
    path('order/delete/<int:pk>/', OrdersEliminarPageView.as_view(), name='order_delete'),
    path('custumer/create', CustumerViewPage.as_view(),name='custumer_create'),
    #path('custumer/edit/<int:pk>/', CustumersEditarViewPage.as_view(), name='custumer_edit')
]