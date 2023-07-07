from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User, UserProfile



# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin')}),
    
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email',"password1", "password2", 'first_name', 'last_name'),
        }),
    )

    list_display = ["email","username", "first_name",'role', "is_admin"]
    list_filter = ["is_admin"]
    search_fields = ["email"]
    ordering = ["-date_joined"]
    filter_horizontal = []

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.unregister(Group)
