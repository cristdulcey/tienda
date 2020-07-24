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
    list_display = ("date", "state")
    list_display_links = ("date", "state")
    raw_id_fields = ("category", "shop")
    search_fields = ("date","name")
    list_filter = ("state","client__name")

@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    
    list_display = ("shop", "order", "staff")
    list_display_links = ("shop", "order", "staff")
    raw_id_fields = ("shop", "staff","order")
    search_fields = ("shop__name",)
    list_filter = ("shop",)

@admin.register(OrderProduct)
class AdminOrderProduct(admin.ModelAdmin):
    list_display = ("quantity", "value_unit","value_total")
    list_display_links = ("quantity", "value_unit","value_total")
    raw_id_fields = ("order", "product")
    search_fields = ("product__name", "order__id")
    