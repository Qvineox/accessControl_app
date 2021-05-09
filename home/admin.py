from django.contrib import admin

from .models import Entry


class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Entry)
class AdminResources(admin.ModelAdmin):
    list_display = ('id', 'author', 'executor', 'status', 'created_at', 'granted_at', 'expired_at', 'resource')
    list_filter = ('status', 'author')

    fieldsets = (
        ('Агенты доступа', {
            'fields': ('author', 'executor', 'resource')
        }),
        ('Даты действия', {
            'fields': ('granted_at', 'expired_at')
        }),
        ('Статус заявки', {
            'fields': ['status']
        }),
    )
