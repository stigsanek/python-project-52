from django.contrib.auth.forms import UserCreationForm
from task_manager.users.models import AppUser


class UserForm(UserCreationForm):
    """Form for user creation and update"""

    class Meta:
        model = AppUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]
