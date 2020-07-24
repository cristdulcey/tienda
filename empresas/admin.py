from django.contrib import admin

# Register your models here.
from empresas.models import Shop
from productos.models import Product
from compras.models import Cupon
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

@admin.register(Shop)
class AdminShop(admin.ModelAdmin):
    list_display = ["name", "nit", "address", "state"]
    list_display_links = ["name", "nit", "address"]
    raw_id_fields = []
    search_fields = ["name", "nit"]
    list_filter = ["state"]
    inlines = [CuponInline, ProductInline ]