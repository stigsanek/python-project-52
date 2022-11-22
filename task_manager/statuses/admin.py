from django.contrib import admin

from task_manager.statuses import models


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
