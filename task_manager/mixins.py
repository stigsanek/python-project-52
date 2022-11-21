from django.contrib.messages import error, success
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class CheckSignInMixin:
    """Custom mixin for sign in user"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            error(
                request,
                _('Вы не авторизованы! Пожалуйста, выполните вход.')
            )
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


class ChangeUserMixin:
    """Custom mixin for update or delete user"""

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            error(
                request,
                _('У вас нет прав для изменения другого пользователя.')
            )
            return redirect(reverse_lazy('users:list'))

        return super().dispatch(request, *args, **kwargs)


class DeleteRelatedEntityMixin:
    """Custom mixin for delete related entities"""
    error_message = ''
    success_message = ''

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            error(self.request, self.error_message)
        else:
            success(self.request, self.success_message)

        success_url = self.get_success_url()
        return redirect(success_url)
