from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    """Label model"""
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
        verbose_name = _('метка')
        verbose_name_plural = _('метки')

    def __str__(self):
        return self.name
