from django.contrib import admin

# Register your models here.
from productos.models import Category, Unit, Product
from compras.models import Cupon, OrderProduct
from jet.admin import CompactInline
from empresas.admin import ProductInline

class CuponInline(admin.StackedInline):#CompactInline, TabularInline
    model = Cupon
    extra = 0
    raw_id_fields = ("shop","category",)

class OrderProductInline(admin.StackedInline):#CompactInline, TabularInline
    model = OrderProduct
    extra = 0
    raw_id_fields = ("order","product",)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    raw_id_fields = ("parent",)
    search_fields = ("name",)
    list_filter = ("name",)
    inlines = [CuponInline,ProductInline]

class ProductInlines(admin.StackedInline):
    model = Product
    extra = 0
    raw_id_fields = ("category","shop")

@admin.register(Unit)
class AdminUnit(admin.ModelAdmin):
    list_display = ("name","description")
    list_display_links = ("name",)
    #raw_id_fields = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    inlines = [ProductInline,]

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ("name","valor","quantity","category")
    list_display_links = ("name","valor","quantity","category")
    raw_id_fields = ("category","unidades")
    search_fields = ("name",)
    list_filter = ("category",)
    inlines = [OrderProductInline,]