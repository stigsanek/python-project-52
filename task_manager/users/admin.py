from django.contrib import admin
from task_manager.users import models


@admin.register(models.AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('name',)
