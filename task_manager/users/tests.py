from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

FAKE_PASSWORD = 'Fake_pass1!2@'


class TestUsers(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.users = User.objects.all()
        self.first_user = User.objects.get(pk=1)
        self.second_user = User.objects.get(pk=2)

    def test_user_list(self):
        """Test for user list page"""
        resp = self.client.get(reverse('users:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(
            qs=resp.context['users'],
            values=self.users,
            ordered=False
        )

    def test_sign_in(self):
        """Test for sign in user"""
        resp = self.client.post(
            path=reverse('login'),
            data={
                'username': self.first_user.username,
                'password': FAKE_PASSWORD
            },
            follow=True
        )

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Выход')
        self.assertContains(resp, 'Вы залогинены')
        self.assertNotContains(resp, 'Вход')

    def test_sign_out(self):
        """Test for sign out user"""
        self.client.force_login(self.first_user)
        resp = self.client.post(reverse('logout'))

        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('home'))

    def test_create_user(self):
        """Test for create user"""
        resp = self.client.post(
            path=reverse('users:create'),
            data={
                'username': 'test',
                'password1': FAKE_PASSWORD,
                'password2': FAKE_PASSWORD,
            },
            follow=True
        )

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Пользователь успешно зарегистрирован')

        user = User.objects.filter(username='test').first()
        self.assertIsNotNone(user)
