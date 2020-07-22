from django.contrib import admin

# Register your models here.
from productos.models import Category, Unit, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass

@admin.register(Unit)
class AdminUnit(admin.ModelAdmin):
    pass

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass