from django.contrib import admin
from task_manager.labels import models


@admin.register(models.Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
