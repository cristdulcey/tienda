from django.contrib import admin

# Register your models here.
from productos.models import Category, Unit, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    raw_id_fields = ("parent",)
    search_fields = ("name",)
    list_filter = ("name",)

@admin.register(Unit)
class AdminUnit(admin.ModelAdmin):
    list_display = ("name","description")
    list_display_links = ("name",)
    #raw_id_fields = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ("name","valor","quantity","category")
    list_display_links = ("name","valor","quantity","category")
    raw_id_fields = ("category","unidades")
    search_fields = ("name",)
    list_filter = ("category",)