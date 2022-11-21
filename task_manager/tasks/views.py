from django.contrib.auth.models import User
from django.contrib.messages import error
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from task_manager.mixins import CheckSignInMixin
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


class TaskListView(CheckSignInMixin, ListView):
    """All tasks"""
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'


class DetailTaskView(CheckSignInMixin, DetailView):
    """Detail task"""
    model = Task
    template_name = 'tasks/detail.html'


class CreateTaskView(CheckSignInMixin, SuccessMessageMixin, CreateView):
    """Create task"""
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_message = _('Задача успешно создана')
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        author = User.objects.get(pk=self.request.user.pk)
        form.instance.author = author
        return super().form_valid(form)


class UpdateTaskView(CheckSignInMixin, SuccessMessageMixin, UpdateView):
    """Update task"""
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_message = _('Задача успешно изменена')
    success_url = reverse_lazy('tasks:list')


class DeleteTaskView(CheckSignInMixin, SuccessMessageMixin, DeleteView):
    """Delete task"""
    model = Task
    template_name = 'tasks/delete.html'
    success_message = _('Задача успешно удалена')
    success_url = reverse_lazy('tasks:list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object().author:
            error(
                request,
                _('Задачу может удалить только её автор')
            )
            return redirect(reverse_lazy('tasks:list'))
        return super().dispatch(request, *args, **kwargs)
