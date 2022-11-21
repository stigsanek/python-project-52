from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status


class TestStatuses(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.statuses = Status.objects.all()
        self.first_status = Status.objects.get(pk=1)
        self.second_status = Status.objects.get(pk=3)

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
        self.assertTrue(
            Status.objects.filter(name='test').exists()
        )

    def test_update_status(self):
        """Test for update status"""
        url = reverse('statuses:update', args=[self.first_status.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.post(path=url, data={'name': 'test'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Статус успешно изменён')
        self.assertTrue(
            Status.objects.filter(name='test').exists()
        )

    def test_delete_status(self):
        """Test for delete status"""
        url = reverse('statuses:delete', args=[self.second_status.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.post(path=url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Статус успешно удалён')

        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=self.second_status.id)

    def test_delete_with_tasks(self):
        """Test for delete status with tasks"""
        url = reverse('statuses:delete', args=[self.first_status.id])
        self.client.force_login(self.user)

        resp = self.client.post(path=url, follow=True)
        self.assertContains(
            resp,
            'Невозможно удалить статус, потому что он используется'
        )
        self.assertTrue(
            Status.objects.filter(pk=self.first_status.id).exists()
        )
