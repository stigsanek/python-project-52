from django.contrib import admin

from task_manager.tasks import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'author', 'executor')
    list_filter = ('status',)
