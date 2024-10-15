from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {
            'fields': ('birthday', 'phone_number',)
            }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {
            'fields': ('birthday', 'phone_number',),
        }),
    )
    
admin.site.register(User, UserAdmin)