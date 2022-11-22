import django_filters
from django.contrib.auth.models import User
from django.db.models import Value
from django.db.models.functions import Concat
from django.forms import CheckboxInput
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class TaskFilter(django_filters.FilterSet):
    """Filter for Task model"""
    status = django_filters.ChoiceFilter(
        choices=Status.objects.values_list('id', 'name').order_by('id')
    )
    executor = django_filters.ChoiceFilter(
        choices=User.objects.values_list(
            'id', Concat('first_name', Value(' '), 'last_name')
        ).order_by('id')
    )
    label = django_filters.ChoiceFilter(
        label=_('Метка'),
        choices=Label.objects.values_list('id', 'name').order_by('id'),
        field_name='labels'
    )
    self_tasks = django_filters.BooleanFilter(
        label=_('Только свои задачи'),
        widget=CheckboxInput(),
        method='filter_self_tasks'
    )

    def filter_self_tasks(self, qs, name, value):
        if value:
            qs = qs.filter(author=self.request.user).order_by('id')
        return qs
