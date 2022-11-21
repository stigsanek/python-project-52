from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from task_manager.tasks.models import Task


class TestTasks(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    def setUp(self):
        self.first_user = User.objects.get(pk=1)
        self.second_user = User.objects.get(pk=2)
        self.tasks = Task.objects.all()
        self.first_task = Task.objects.get(pk=1)
        self.second_task = Task.objects.get(pk=3)

    def test_task_list(self):
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
            values=self.tasks,
            ordered=False
        )

    def test_create_task(self):
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

    def test_update_task(self):
        """Test for update task"""
        url = reverse('tasks:update', args=[self.first_task.id])

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

    def test_delete_task(self):
        """Test for delete task"""
        del_url_first = reverse('tasks:delete', args=[self.first_task.id])
        del_url_second = reverse('tasks:delete', args=[self.second_task.id])

        resp = self.client.get(del_url_first)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(self.first_user)

        resp = self.client.post(path=del_url_second, follow=True)
        self.assertContains(resp, 'Задачу может удалить только её автор')
        self.assertTrue(
            Task.objects.filter(pk=self.second_task.id).exists()
        )

        resp = self.client.post(path=del_url_first, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Задача успешно удалена')

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.first_task.id)
