from django.contrib import admin

# Register your models here.
from compras.models import Cupon, Order, Notification, OrderProduct


@admin.register(Cupon)
class AdminCupon(admin.ModelAdmin):
    pass

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass

@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    pass

@admin.register(OrderProduct)
class AdminOrderProduct(admin.ModelAdmin):
    pass