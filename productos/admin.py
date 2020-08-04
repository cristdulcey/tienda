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

class ProductInline(admin.StackedInline):
    model = Product
    extra = 0
    raw_id_fields = ("unidades","shop")

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
    list_display = ("name","value","quantity","category")
    list_display_links = ("name","value","quantity","category")
    raw_id_fields = ("category","unidades","shop")
    search_fields = ("name",)
    list_filter = ("category",)
    inlines = [OrderProductInline,]
    actions = ("set_value_product",)
    ordering = ("-name",)
   # readonly_fields = ("quantity",)
    def set_value_product(self,request,queryset):
        for a in queryset:
            a.value = 1000
            a.save()
            self.message_user(request, '{} {} {}'.format("Producto", a.name,"ha sido actualizado"))

    set_value_product.short_description = "Poner precio $1000"
