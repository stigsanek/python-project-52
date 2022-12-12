from django.contrib import admin
from task_manager.tasks import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'status', 'author', 'executor', 'created_at', 'updated_at'
    )
    list_filter = ('status', 'author', 'executor', 'labels')
    search_fields = ('name',)
