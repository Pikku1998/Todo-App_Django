from django.urls import path
from .views import TaskList, TaskDetail, CreateTask

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('create-task', CreateTask.as_view(), name='create_task'),
    
]