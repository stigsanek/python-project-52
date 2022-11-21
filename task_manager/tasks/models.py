from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


class Task(models.Model):
    """Task model"""
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text=_('Обязательное поле. Не более 150 символов.'),
        verbose_name=_('Имя')
    )
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    status = models.ForeignKey(
        to=Status,
        on_delete=models.PROTECT,
        related_name='task_status',
        verbose_name=_('Статус')
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='task_author',
        verbose_name=_('Автор')
    )
    executor = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='task_executor',
        null=True,
        blank=True,
        verbose_name=_('Исполнитель')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')

    def __str__(self):
        return self.name
