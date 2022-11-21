from django.urls import path

from task_manager.labels import views

urlpatterns = [
    path('', views.ListLabelView.as_view(), name='list'),
    path('create/', views.CreateLabelView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateLabelView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteLabelView.as_view(), name='delete'),
]
