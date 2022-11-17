from django.contrib.auth.models import User
from django.views.generic import ListView


class UserListView(ListView):
    """View all users"""
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
