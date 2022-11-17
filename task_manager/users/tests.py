from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy


class TestUsers(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.users = User.objects.all()
        self.first_user = User.objects.get(pk=1)
        self.second_user = User.objects.get(pk=2)

    def test_user_list_view(self):
        """Test for user list page"""
        resp = self.client.get(reverse_lazy('users:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(
            resp.context['users'],
            self.users,
            ordered=False
        )
