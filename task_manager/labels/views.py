from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.mixins import CheckSignInMixin, DeleteRelatedEntityMixin


class ListLabelView(CheckSignInMixin, ListView):
    """All labels"""
    model = Label
    template_name = 'labels/list.html'
    context_object_name = 'labels'


class CreateLabelView(CheckSignInMixin, SuccessMessageMixin, CreateView):
    """Create label"""
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_message = _('Метка успешно создана')
    success_url = reverse_lazy('labels:list')


class UpdateLabelView(CheckSignInMixin, SuccessMessageMixin, UpdateView):
    """Update label"""
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_message = _('Метка успешно изменена')
    success_url = reverse_lazy('labels:list')


class DeleteLabelView(CheckSignInMixin, DeleteRelatedEntityMixin, DeleteView):
    """Delete label"""
    model = Label
    template_name = 'labels/delete.html'
    success_message = _('Метка успешно удалена')
    error_message = _('Невозможно удалить метку, потому что она используется')
    success_url = reverse_lazy('labels:list')
