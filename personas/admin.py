from django.contrib import admin

# Register your models here.
from personas.models import Client


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    pass