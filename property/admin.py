from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['town', 'address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


admin.site.register(Flat, FlatAdmin)
