from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status


class TestStatuses(TestCase):
    fixtures = ['statuses.json', 'users.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.statuses = Status.objects.all()
        self.status = Status.objects.get(pk=1)

    def test_status_list(self):
        """Test for status list page"""
        url = reverse('statuses:list')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(
            qs=resp.context['statuses'],
            values=self.statuses,
            ordered=False
        )

    def test_create_status(self):
        """Test for create status"""
        url = reverse('statuses:create')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.post(path=url, data={'name': 'test'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Статус успешно создан')

        status = Status.objects.filter(name='test').first()
        self.assertIsNotNone(status)

    def test_update_status(self):
        """Test for update status"""
        url = reverse('statuses:update', args=[self.status.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.post(path=url, data={'name': 'test'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Статус успешно изменён')

        status = Status.objects.filter(name='test').first()
        self.assertIsNotNone(status)

    def test_delete_status(self):
        """Test for delete status"""
        url = reverse('statuses:delete', args=[self.status.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.post(path=url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Статус успешно удалён')

        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=self.status.id)
