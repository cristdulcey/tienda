from django.contrib import admin

# Register your models here.
from personas.models import Client, Staff


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    pass
@admin.register(Staff)
class AdminStaff(admin.ModelAdmin):
    pass