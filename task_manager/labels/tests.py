from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label


class TestLabels(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.first_label = Label.objects.get(pk=1)
        self.second_label = Label.objects.get(pk=2)

    def test_list(self):
        """Test for label list page"""
        url = reverse('labels:list')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(
            qs=resp.context['labels'],
            values=Label.objects.all(),
            ordered=False
        )

    def test_create(self):
        """Test for create label"""
        url = reverse('labels:create')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.post(path=url, data={'name': 'test'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Метка успешно создана')
        self.assertTrue(
            Label.objects.filter(name='test').exists()
        )

    def test_update(self):
        """Test for update label"""
        url = reverse('labels:update', args=[self.first_label.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.post(path=url, data={'name': 'test'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Метка успешно изменена')
        self.assertTrue(
            Label.objects.filter(name='test').exists()
        )

    def test_delete(self):
        """Test for delete label"""
        url = reverse('labels:delete', args=[self.second_label.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.user)

        resp = self.client.post(path=url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Метка успешно удалена')

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=self.second_label.id)

    def test_delete_with_tasks(self):
        """Test for delete label with tasks"""
        url = reverse('labels:delete', args=[self.first_label.id])
        self.client.force_login(self.user)

        resp = self.client.post(path=url, follow=True)
        self.assertContains(
            resp,
            'Невозможно удалить метку, потому что она используется'
        )
        self.assertTrue(
            Label.objects.filter(pk=self.first_label.id).exists()
        )
