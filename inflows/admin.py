from django.contrib import admin
from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'supplier', 'quantity', 'description', 'created_at', 'updated_at')
    search_fields = ('id', 'product', 'supplier', 'created_at', 'updated_at')
