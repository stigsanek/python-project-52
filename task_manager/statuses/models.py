from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    """Status model"""
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text=_('Обязательное поле. Не более 150 символов.'),
        verbose_name=_('имя')
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
        verbose_name = _('статус')
        verbose_name_plural = _('статусы')

    def __str__(self):
        return self.name
