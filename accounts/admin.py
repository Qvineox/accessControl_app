from django.contrib import admin

from .models import Employee, Division


class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class AdminEmployees(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'email', 'division', 'account')
    list_filter = ['division']

    fieldsets = (
        ('Персональные данные', {
            'fields': ('first_name', 'last_name', 'middle_name')
        }),
        ('Контакты', {
            'fields': ('email', 'account')
        }),
        ('Отдел организации', {
            'fields': ['division']
        }),
    )


@admin.register(Division)
class AdminDivisions(admin.ModelAdmin):
    list_display = ('id', 'name', 'head')
