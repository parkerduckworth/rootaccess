from django.contrib import admin
from academy.models import Student, Module


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Membership Information', {
            'fields': ('user_name', 'email', 'password', 'current_module')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'location')
        }),
    )


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'details')
