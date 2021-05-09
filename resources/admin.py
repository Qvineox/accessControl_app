from django.contrib import admin

from .models import Resource, Facility


class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Resource)
class AdminResources(admin.ModelAdmin):
    list_display = ('id', 'name', 'DNS_address', 'admin', 'owner')
    list_filter = ['facility']

    fieldsets = (
        ('Описание', {
            'fields': ('name', 'description', 'facility')
        }),
        ('Местоположение', {
            'fields': ['DNS_address']
        }),
        ('Ответсвенные лица', {
            'fields': ('owner', 'admin')
        }),
    )


@admin.register(Facility)
class AdminFacilities(admin.ModelAdmin):
    list_display = ('id', 'name', 'DNS_address', 'location', 'admin', 'owner')

    fieldsets = (
        ('Описание', {
            'fields': ('name', 'description')
        }),
        ('Местоположение', {
            'fields': ('location', 'DNS_address')
        }),
        ('Ответсвенные лица', {
            'fields': ('owner', 'admin')
        }),
    )
