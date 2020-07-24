from django.contrib import admin

# Register your models here.
from compras.models import Cupon, Order, Notification, OrderProduct


@admin.register(Cupon)
class AdminCupon(admin.ModelAdmin):
    list_display = ("name","code")
    list_display_links = ("name","code")
    raw_id_fields = ("category","shop")
    search_fields = ("category__name",)
    list_filter = ("category",)


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass

@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    
    list_display = ("shop", "order", "staff")
    list_display_links = ("shop", "order", "staff")
    raw_id_fields = ("shop", "staff","order")
    search_fields = ("shop__name",)
    list_filter = ("shop",)

@admin.register(OrderProduct)
class AdminOrderProduct(admin.ModelAdmin):
    pass