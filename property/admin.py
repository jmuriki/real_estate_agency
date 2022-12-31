from django.contrib import admin

from .models import Flat, Complaint, Owner


class AdminInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ['owner', 'flat']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['town', 'address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [AdminInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owned_flats']
    inlines = [AdminInline]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
