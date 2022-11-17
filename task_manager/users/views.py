from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages import add_message, SUCCESS
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView

from task_manager.users.forms import CreateUserForm


class UserListView(ListView):
    """All users"""
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'


class SignInView(SuccessMessageMixin, LoginView):
    """Sign in user"""
    model = User
    template_name = 'users/sign_in.html'
    success_message = _('Вы залогинены')
    next_page = reverse_lazy('home')


class SignOutView(SuccessMessageMixin, LogoutView):
    """Sign out user"""
    success_message = _('Вы разлогинены')
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        add_message(
            request=request,
            level=SUCCESS,
            message=self.success_message
        )
        return super().dispatch(request, *args, **kwargs)


class CreateUserView(SuccessMessageMixin, CreateView):
    """Create user"""
    model = User
    form_class = CreateUserForm
    template_name = 'users/create.html'
    success_message = _('Пользователь успешно зарегистрирован')
    success_url = reverse_lazy('login')
