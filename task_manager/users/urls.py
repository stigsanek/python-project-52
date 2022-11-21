from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('', views.ListUserView.as_view(), name='list'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateUserView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteUserView.as_view(), name='delete'),
]
