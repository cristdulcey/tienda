from django.contrib import admin

# Register your models here.
from empresas.models import Shop
from productos.models import Product
from compras.models import Cupon, Notification
from jet.admin import CompactInline
from personas.models import Staff
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