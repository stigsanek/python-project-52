from django.urls import path

from task_manager.tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:pk>/', views.DetailTaskView.as_view(), name='detail'),
    path('create/', views.CreateTaskView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateTaskView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete'),
]
