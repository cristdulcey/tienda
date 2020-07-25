from django.contrib import admin

# Register your models here.

from compras.models import Order
from personas.models import Client, Staff

class OrderInlines(admin.StackedInline):
    model = Order
    extra = 0

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ("user", "phone")
    list_display_links = ("user", "phone")
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