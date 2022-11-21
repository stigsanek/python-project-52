from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.tasks.models import Task


class TestTasks(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']

    def setUp(self):
        self.task = Task.objects.get(pk=1)
        self.first_user = User.objects.get(pk=1)
        self.second_user = User.objects.get(pk=2)

    def test_list(self):
        """Test for task list page"""
        url = reverse('tasks:list')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.first_user)

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(
            qs=resp.context['tasks'],
            values=Task.objects.all(),
            ordered=False
        )

    def test_create(self):
        """Test for create task"""
        url = reverse('tasks:create')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.first_user)

        resp = self.client.post(
            path=url,
            data={
                'name': 'test',
                'description': 'test',
                'status': '1',
                'executor': '1',
            },
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Задача успешно создана')

        task_qs = Task.objects.filter(name='test')
        self.assertTrue(task_qs.exists())
        self.assertEqual(task_qs.first().author_id, self.first_user.id)

    def test_update(self):
        """Test for update task"""
        url = reverse('tasks:update', args=[self.task.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.first_user)

        resp = self.client.post(
            path=url,
            data={
                'name': 'test',
                'description': 'test',
                'status': '1',
                'executor': '2',
            },
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Задача успешно изменена')
        self.assertTrue(
            Task.objects.filter(name='test').exists()
        )

    def test_delete(self):
        """Test for delete task"""
        url = reverse('tasks:delete', args=[self.task.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.first_user)

        resp = self.client.post(path=url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Задача успешно удалена')

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.task.id)

    def test_delete_on_author(self):
        """Test for delete task on author"""
        url = reverse('tasks:delete', args=[self.task.id])
        self.client.force_login(self.second_user)

        resp = self.client.post(path=url, follow=True)
        self.assertContains(resp, 'Задачу может удалить только её автор')
        self.assertTrue(
            Task.objects.filter(pk=self.task.id).exists()
        )
