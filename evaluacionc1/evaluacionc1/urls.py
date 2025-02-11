from django.contrib import admin
from django.urls import path
from .view import OrderListView, OrderCreateView, OrderEditView, OrderDeleteView, HomePageView, RealizarOrdenView, AsignarRepartidorView, OrdenDetalleView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ordenes/ver', OrderListView.as_view(), name="lista_de_ordenes"),
    path('ordenes/crear', OrderCreateView.as_view(), name="crear_orden"),
    path('ordenes/editar/', OrderEditView.as_view(), name="editar_orden"),
    path('ordenes/eliminar/', OrderDeleteView.as_view(), name="eliminar_orden"),
    path('', HomePageView.as_view(), name='home'),
    path('orden/realizar/', RealizarOrdenView.as_view(), name='realizar_orden'),
    path('orden/asignar_repartidor/', AsignarRepartidorView.as_view(), name='asignar_repartidor'),
    path('orden/detalle/', OrdenDetalleView.as_view(), name='orden_detalle'),
]
