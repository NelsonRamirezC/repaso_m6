from django.contrib import admin
from .models import Vehiculo


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['marca', 'tipo']
    list_display = ['marca', 'modelo', 'tipo', 'create_at', 'update_at']
    ordering = ['marca']
    list_filter = ['tipo', 'marca']
    