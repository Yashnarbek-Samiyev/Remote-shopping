from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_manager', 'is_active')
    list_filter = ('is_manager', 'is_active')
    search_fields = ('email', 'full_name')
    ordering = ('email',)
