from django.contrib import admin

# Register your models here.
from empresas.models import Shop


@admin.register(Shop)
class AdminShop(admin.ModelAdmin):
    pass