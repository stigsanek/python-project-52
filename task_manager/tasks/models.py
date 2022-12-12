from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import AppUser


class Task(models.Model):
    """Task model"""
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text=_('Обязательное поле. Не более 150 символов.'),
        verbose_name=_('имя')
    )
    description = models.TextField(blank=True, verbose_name=_('описание'))
    status = models.ForeignKey(
        to=Status,
        on_delete=models.PROTECT,
        related_name='status_tasks',
        verbose_name=_('статус')
    )
    author = models.ForeignKey(
        to=AppUser,
        on_delete=models.PROTECT,
        related_name='author_tasks',
        verbose_name=_('автор')
    )
    executor = models.ForeignKey(
        to=AppUser,
        on_delete=models.PROTECT,
        related_name='executor_tasks',
        null=True,
        blank=True,
        verbose_name=_('исполнитель')
    )
    labels = models.ManyToManyField(
        to=Label,
        related_name='label_tasks',
        blank=True,
        through='TaskLabel',
        through_fields=('task', 'label'),
        verbose_name=_('метки')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('дата создания')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('дата обновления')
    )

    class Meta:
        verbose_name = _('задача')
        verbose_name_plural = _('задачи')

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    """Through model for Task and Label"""
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    label = models.ForeignKey(to=Label, on_delete=models.PROTECT)
