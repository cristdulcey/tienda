from django.contrib import admin

# Register your models here.
from empresas.models import Shop, Staff, Client
from productos.models import Product
from compras.models import Cupon, Notification, Order
from jet.admin import CompactInline

#from productos.admin import CuponInline

class ProductInline(admin.StackedInline):#CompactInline
    model = Product
    extra = 0
    raw_id_fields = ("category", "unidades", "shop",)

class CuponInline(admin.StackedInline):#CompactInline, TabularInline
    model = Cupon
    extra = 0
    raw_id_fields = ("shop","category")

class StaffInline(admin.StackedInline):#CompactInline
    model = Staff
    extra = 0
    raw_id_fields = ("user","shop",)

class NotificationInline(admin.StackedInline):#CompactInline
    model = Notification
    extra = 0
    raw_id_fields = ("staff","shop", "order")

@admin.register(Shop)
class AdminShop(admin.ModelAdmin):
    list_display = ["name", "nit", "address", "state"]
    list_display_links = ["name", "nit", "address"]
    raw_id_fields = []
    search_fields = ["name", "nit"]
    list_filter = ["state"]
    inlines = [CuponInline, ProductInline, NotificationInline, StaffInline ]

class OrderInlines(admin.StackedInline):
    model = Order
    extra = 0

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ("get_full_name_client", "phone")
    list_display_links = ("get_full_name_client", "phone")
    raw_id_fields = ("user",)
    search_fields = ("phone",)
    list_filter = ("user",)
    inlines = [OrderInlines,]

@admin.register(Staff)
class AdminStaff(admin.ModelAdmin):
    list_display = ("user", "type", "shop")
    list_display_links = ("user", "type", "shop")
    raw_id_fields = ("user", "shop")
    search_fields = ("shop__name",)
    list_filter = ("shop",)

