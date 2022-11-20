from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    """Status model"""
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text=_('Обязательное поле. Не более 150 символов.')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Статус')
        verbose_name_plural = _('Статусы')

    def __str__(self):
        return self.__class__.name
