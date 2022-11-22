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
        choices=Status.objects.values_list('id', 'name').all()
    )
    executor = django_filters.ChoiceFilter(
        choices=User.objects.values_list(
            'id', Concat('first_name', Value(' '), 'last_name')
        ).all()
    )
    labels = django_filters.ChoiceFilter(
        choices=Label.objects.values_list('id', 'name').all()
    )
    my_task = django_filters.BooleanFilter(
        label=_('Только свои задачи'),
        widget=CheckboxInput(),
        method='filter_my_tasks'
    )

    def filter_my_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)

        return queryset
