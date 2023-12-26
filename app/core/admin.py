"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'last_name', 'first_name', 'middle_name', 'extension_name', 'contact', 'last_login']
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _('Account Info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'middle_name',
                    'extension_name',
                    'contact'
                )
            }
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']


admin.site.register(models.User, UserAdmin)