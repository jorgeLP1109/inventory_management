from django.contrib import admin
from .models import Proveedor, Producto, Pedido

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Pedido)
