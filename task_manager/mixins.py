from django.contrib.auth.mixins import AccessMixin
from django.contrib.messages import error
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class CheckSignInMixin(AccessMixin):
    """Custom mixin for sign in user"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            error(
                request,
                _('Вы не авторизованы! Пожалуйста, выполните вход.')
            )
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


class ChangeUserMixin(AccessMixin):
    """Custom mixin for update or delete user"""

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            error(
                request,
                _('У вас нет прав для изменения другого пользователя.')
            )
            return redirect(reverse_lazy('users:list'))

        return super().dispatch(request, *args, **kwargs)
