from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

FAKE_PASSWORD = 'Fake_pass1!2@'


class TestUsers(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']

    def setUp(self):
        self.first_user = User.objects.get(pk=1)
        self.second_user = User.objects.get(pk=2)

    def test_list(self):
        """Test for user list page"""
        resp = self.client.get(reverse('users:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(
            qs=resp.context['users'],
            values=User.objects.all(),
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

    def test_create(self):
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
        self.assertTrue(
            User.objects.filter(username='test').exists()
        )

    def test_update(self):
        """Test for update user"""
        url_first = reverse('users:update', args=[self.first_user.id])
        url_second = reverse('users:update', args=[self.second_user.id])

        resp = self.client.get(url_first)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.first_user)

        resp = self.client.get(url_second)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('users:list'))

        resp = self.client.post(
            path=url_first,
            data={
                'username': 'test',
                'password1': FAKE_PASSWORD,
                'password2': FAKE_PASSWORD,
            },
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Пользователь успешно изменён')
        self.assertTrue(
            User.objects.filter(username='test').exists()
        )

    def test_delete(self):
        """Test for delete user"""
        url_first = reverse('users:delete', args=[self.first_user.id])
        url_second = reverse('users:delete', args=[self.second_user.id])

        resp = self.client.get(url_first)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.second_user)

        resp = self.client.get(url_first)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('users:list'))

        resp = self.client.post(path=url_second, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Пользователь успешно удалён')
        self.assertContains(resp, 'Вход')

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=self.second_user.id)

    def test_delete_with_tasks(self):
        """Test for delete user with tasks"""
        url = reverse('users:delete', args=[self.first_user.id])
        self.client.force_login(self.first_user)

        resp = self.client.post(path=url, follow=True)
        self.assertContains(
            resp,
            'Невозможно удалить пользователя, потому что он используется'
        )
        self.assertTrue(
            User.objects.filter(pk=self.first_user.id).exists()
        )
