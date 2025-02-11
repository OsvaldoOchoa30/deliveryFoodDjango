from django.contrib import admin
from django.urls import path
from .view import HomePageView, OrdersCreateViewPage, OrdersEditarPageView, OrdersEliminarPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('order/create/', OrdersCreateViewPage.as_view(), name='order_create'),
    path('order/edit/<int:pk>/', OrdersEditarPageView.as_view(), name='order_edit'),
    path('order/delete/<int:pk>/', OrdersEliminarPageView.as_view(), name='order_delete'),
]
