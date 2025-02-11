# admin.py
from django.contrib import admin
from .models.category import Category
from .models.product import Product
from .models.customer import Customer
from .models.delivery import Delivery
from .models.orders import Orders
from .models.orderProduct import OrderProduct

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    search_fields = ("name", "type")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "amount", "id_category")
    list_filter = ("id_category",)
    search_fields = ("name", "description")

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "phone_number", "address")
    search_fields = ("name", "last_name", "phone_number")

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "status", "phone_number")
    list_filter = ("status",)
    search_fields = ("name", "last_name", "phone_number")

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "id_customer", "id_delivery")
    list_filter = ("date",)
    search_fields = ("id_customer__name", "id_customer__last_name", "id_delivery__name", "id_delivery__last_name")

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("id", "id_order", "id_product")
    list_filter = ("id_order", "id_product")
    search_fields = ("id_order__id", "id_product__name")
