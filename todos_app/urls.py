from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('create-task', CreateTask.as_view(), name='create_task'),
    path('update-task/<int:pk>', UpdateTask.as_view(), name='update_task'),
    
]