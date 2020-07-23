from django.contrib import admin

# Register your models here.
from empresas.models import Shop


@admin.register(Shop)
class AdminShop(admin.ModelAdmin):
    list_display = ["name", "nit", "address", "state"]
    list_display_links = ["name", "nit", "address"]
    raw_id_fields = []
    search_fields = ["name", "nit"]
    list_filter = ["state"]